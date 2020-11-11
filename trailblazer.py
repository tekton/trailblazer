import redis
#
from library import load_config, create_hash, incr_redis, set_redis, get_url
#
from flask import Flask, jsonify, request, redirect


settings = load_config()
pool = redis.ConnectionPool(host=settings["redis"]["host"],
                            port=settings["redis"]["port"],
                            db=settings["redis"]["db"])
global r
r = redis.Redis(connection_pool=pool)
app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(
        {"usage": {
            "/trail": {
                "description": "create a blur to use as a url shortener later",
                "verb": "POST",
                "type": "application/json",
                "variables": {
                    "url": "string of where to redirect"
                }
            },
            "/u/<x>": {
                "description": "get redirected based on the given blur",
                "verb": "GET"
            }
        }})


@app.route('/trail', methods=['POST'])
def trail():
    # print(request)
    data = request.json
    # print(data)
    if "url" not in data:
        return None
    # ask redis for new integter
    num = incr_redis(r, settings)
    blur = create_hash(num)
    rtn_dict = {
        "blur": blur,
        "url": data["url"]
    }
    redis_res = set_redis(r, settings, rtn_dict["blur"], rtn_dict["url"])
    rtn_dict["redis"] = redis_res
    return jsonify(rtn_dict)


@app.route('/u/<blur>')
def blaze(blur):
    url = get_url(r, settings, blur)
    return redirect(url.decode())


if __name__ == "__main__":
    app.run(debug=True)
