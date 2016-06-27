#coding:utf-8
import requests
import urllib
base_url = "http://mp.weixin.qq.com/s?__biz=Mjc1NjM3MjY2MA==&mid=2691310771&idx=3&sn=d308533b2e53e0a086d431389c3093bc#rd"
# requests.get(base_url)
o = urllib.urlretrieve(base_url,"./1.html")
print o 
print "ok"
