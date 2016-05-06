import requests

import json
import base64
import hmac
import hashlib
import base64

signingStr = "<fetch>?<to>\n<body>"
data = ""


def HMAC_SHA1():
    return hmac.new(signingStr, data, hashlib.sha1).digest().encode('base64').rstrip()


def encode_s(item):
    i = base64.b64encode(item)
    return i.replace("+", "_").replace("/", "_")


def test(first, second):
    base = "http://iovip.qbox.me/fetch/{0}/to/{1}".format(first, second)
    headers = {
        "Authorization": "QBox :%s" % HMAC_SHA1()}
    print "headers", headers
    r = requests.post(base, headers=headers)
    print r.text

# entry = "qiniuphotos:gogopher.jpg"
new_entry = "iislookingit:"
first = encode_s(new_entry)
second = encode_s(
    "http://img3.fengniao.com/album/upload/156/31011/6202034.jpg")

test(first, second)
