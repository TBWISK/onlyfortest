# coding:utf-8
import md5
import requests
import uuid
import sys
reload(sys)
sys.setdefaultencoding('utf8')
src = md5.new()

nonce = uuid.uuid4().hex[0:9]
print nonce
rank_name_group = ["资讯", "生活"]
zixuns = ["时事", "民生", "财富", "科技", "创业",
          "汽车", "楼市", "职场", "教育", "学术", "政务", "企业"]
lifes = ["文化", "百科", "健康", "时尚", "美食", "乐活",
         "旅游", "幽默", "情感", "体娱", "美体", "文摘"]
src.update(
    "/xdnphb/list/day/rank?AppKey=joker&end=2016-07-24&rank_name=科技&rank_name_group=资讯&start=2016-07-24&nonce={0}".format(nonce))


base_url = "http://www.newrank.cn/xdnphb/list/day/rank"
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "www.newrank.cn",
    "Origin": "http://www.newrank.cn",
    "Pragma": "no-cache",
    "Referer": "http://www.newrank.cn/public/info/list.html",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

data = {
    "end": "2016-07-24",
    "rank_name": "科技",
    "rank_name_group": "资讯",
    "start": "2016-07-24",
    "nonce": nonce,
    "xyz": src.hexdigest()
}
print "start"
r = requests.post(base_url, headers=headers, data=data)
items = (r.json().get("value"))
for item in items:
    print item.get("biz_info"), item.get("account"), item.get("name")
# print len(item)
