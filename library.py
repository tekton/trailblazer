import random
import base64 # base64.urlsafe_b64encode
import time
import redis


def load_config(loc="./config.json"):
    # load the configuration file to figure out where things are supposed to be
    return {
        "root": "trailblazer",
        "redis": {
            "host": "localhost",
            "port": 6379,
            "db": 0
        }
    }


def create_seeded_hash(blur):
    b = base64.b64encode(hex(random.randint(0, 1000))[2:])
    t = base64.b64encode(hex(int(time.time() % 1000))[2:])
    z = base64.b64encode(hex(blur)[2:])
    # print("{}{}{}".format(b, t, z))


def create_hash(blur):
    x = hex(blur)[2:]
    x = x.encode()
    z = base64.b64encode(x)
    # print("{}".format(z))
    return str(z.decode())


def incr_redis(r, settings):
    key = "{}_inc:int".format(settings["root"])
    num = r.incr(key)
    num = int(num)
    return num


def set_redis(r, settings, blur, url):
    key = "{}:hash".format(settings["root"])
    res = r.hset(key, blur, url)
    return res


def get_url(r, settings, blur):
    key = "{}:hash".format(settings["root"])
    res = r.hget(key, blur)
    return res
