
from hashlib import md5
import datetime
import random


def shortener(url):
    url = "{}{}".format(url, datetime.datetime.now().strftime("%f"))
    url = bytes(url, encoding="ascii")
    m = md5()
    m.update(url)
    return "".join([random.choice(m.hexdigest()) for _ in range(6)])
