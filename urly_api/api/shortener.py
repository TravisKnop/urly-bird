
from hashlib import md5
import datetime
import random
from api import models


def shortener(long_url, form):
    input = "{}{}{}".format(form.instance.long_url, datetime.datetime.now().strftime("%f"))
    url_code = bytes(input, encoding="ascii")
    m = md5(url_code)
    m.update(url_code)
    short_url_code = m.hexdigest()
    short_url = "tk" + short_url_code[:8]
    return super().form_valid(form)
