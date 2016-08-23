# coding:utf-8
import requests
import re


def get_recommend_id():
    base_url = "http://www.gsdata.cn/rank/single?id=MxTuAez5M2j1Etza"
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "www.gsdata.cn",
        "Origin": "http://www.newrank.cn",
        "Pragma": "no-cache",
        "Referer": "http://www.gsdata.cn/themes/search_2016/css/index.css",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    r = requests.get(base_url, headers=headers)
    html_re = r'"id":.*},'
    dr = re.findall(html_re, r.content)
    if dr:
        item = dr[0].replace('"id":"', "").replace('"},', "")
        print item


def get_recommendArticles(item_id):
    url = "http://www.gsdata.cn/rank/recommendArticles?id=%s&type=recently" % item_id
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate,sdch",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "www.gsdata.cn",
        # "Origin": "www.gsdata.cn",
        "Pragma": "no-cache",
        "Cookie": "PHPSESSID=058pq711fr8tn7biv8gbf6t8i0",
        "Referer": "http://www.gsdata.cn/rank/single?id=MxTuAe35N2T1Ytya",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    r = requests.get(url, headers=headers)
    js = r.json()
    print js
    items = js.get("result").get("items")
    print items
    print items[0].get("url")

get_recommendArticles(888)


def get_detail():
    pass
