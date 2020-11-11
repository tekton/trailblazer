import random
import base64  # base64.urlsafe_b64encode
import time
import json


def load_config(loc="./config.json"):
    with open(loc, "r") as infile:
        return json.load(infile)


def create_seeded_hash(blur):
    b = base64.b64encode(hex(random.randint(0, 1000))[2:])
    t = base64.b64encode(hex(int(time.time() % 1000))[2:])
    z = base64.b64encode(hex(blur)[2:])
    return "{}{}{}".format(b, t, z)


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


def set_redis(r, settings, blur, url, ttl=604800):  # TTL = 7 days
    _key = "{}:{}:url".format(settings["root"], blur)
    _res = r.set(_key, url)
    _ex = r.expire(_key, ttl)
    # print(_res, _ex)

    # key = "{}:hash".format(settings["root"])
    # res = r.hset(key, blur, url)
    return _res


def get_url(r, settings, blur):
    _key = "{}:{}:url".format(settings["root"], blur)
    _res = r.get(_key)
    # print(_res)

    # key = "{}:hash".format(settings["root"])
    # res = r.hget(key, blur)
    return _res
