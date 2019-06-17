import random
import base64 # base64.urlsafe_b64encode
import time
import redis
#
from library import load_config, create_hash, incr_redis, set_redis, get_url
#
from flask import Flask, jsonify, render_template, request, redirect


settings = load_config()
pool = redis.ConnectionPool(host=settings["redis"]["host"],
                            port=settings["redis"]["port"],
                            db=settings["redis"]["db"])
r = redis.Redis(connection_pool=pool)
app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"msg": "WAT"})


@app.route('/trail', methods=['POST'])
def trail():
    data = request.json
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
    return redirect(url)


if __name__ == "__main__":
	pass