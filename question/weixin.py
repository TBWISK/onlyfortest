# coding:utf-8
from requests.exceptions import ConnectionError, HTTPError
import requests
import re


def _getHead():
    return "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn;\
HM 2A Build/KTU84Q) AppleWebKit/533.1 \
(KHTML, like Gecko)Version/4.0 MQQBrowser/5.4 \
TBS/025489 Mobile Safari/533.1 MicroMessenger/6.3.13.49_r4080b63.740 \
NetType/WIFI Language/zh_CN"


def getOriginText(url):
    """
    获取原始的网页信息
    """
    r = None
    try:
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/sharpp,*/*;q=0.8",
            "Accept-Encoding": "gzip,deflate",
            "Accept-Languagxe": "zh-CN,en-US;q=0.8",
            "User-Agent": _getHead()
        }
        r = requests.get(url, headers=headers)
        return str(r.content)
    except ConnectionError as e:
        print e
        return None
    except HTTPError as e:
        print e
        return None
    except Exception as e:
        print e
        return None
    finally:
        if r:
            r.close()


def test():
    # url =
    # "http://mp.weixin.qq.com/s?__biz=MjM5OTIwODMzMQ==&mid=2674375840&idx=1&sn=2e784e59ec878bb8ee91650ea79eaa9a#rd"
    # url = "http://mp.weixin.qq.com/s?src=3&timestamp=1472460126&ver=1&signature=BX7fCkXKcdRlBkAOenphiVGBV9onm97hqSp7tBu4Tp6ZVRfuB*jAQQJWb5aKgWcYXjaxFv57Xe*OIdI*x33SHKiJbtC8iU2AYPqZ2cjE8KERHcznUuJkfiPZohGSNgPsG4nbLLINZACHKadvrZS3AQB8lk1PBkABDQ*bCwptjr0="
    url = "http://mp.weixin.qq.com/s?__biz=MjM5NzI2NjMwMA==&mid=2651440750&idx=1&sn=165ed6728331ff96078c5ec882e797d0&scene=1&srcid=08293IxOGSnCDjm243glUhzZ#rd"
    text = getOriginText(url)
    copy = 'id="copyright_logo"'
    items = re.findall(copy, text)
    if items:
        print items
    else:
        print False

    audio = 'audio_iframe'
    items = re.findall(audio, text)
    if items:
        print items
    else:
        print False
    videos = "video_iframe"
    items = re.findall(videos, text)
    if items:
        print items
    else:
        print False


test()
