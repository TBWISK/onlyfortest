# coding:utf-8

import urllib3
import json


def connect_lauch_user(user_id, http):
    data = {'data': ["1", "2", "3"], 'user_id': user_id}
    encoded_data = json.dumps(data).encode('utf-8')
    r = http.request(
        "POST", "http://127.0.0.1:8000/h/conlia_valentines/lanuch_post_tags/",
        body=encoded_data,
        headers={'Content-Type': 'application/json'})
    print r.status, json.loads(r.data.decode('utf-8'))['json']


def connect_index(user_id):
    http = urllib3.PoolManager()
    r = http.request(
        'GET', 'http://127.0.0.1:8000/h/conlia_valentines/index/?user_id={0}#!/index'.format(user_id))
    print r.status, r.data

connect_index(1)
