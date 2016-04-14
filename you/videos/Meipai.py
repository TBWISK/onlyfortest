#coding:utf-8
#用于获取网页内的视频地址
#这个是获取 秒拍
import urllib2
import json
import urllib
import urlparse
# from bs4 import BeautifulSoup
import json
def getMiaoPai(url):

	# url = "http://m.miaopai.com/show/channel/HYTXfJLr~gc9YgQm2kGiNQ__"
	# url = "http://ent.v.sina.cn/show/n3wzZeulwgynFhBMjYXMbQ__.htm"
	base = "http://stream.yixia.com/stream/{1}.json?os=android&uuid=06dd2de1-d035-3acb-a331-fd478dd85e47&channel=xiaomi&deviceId=52c33cfb8ac75ece&vend=miaopai&version=6.2.3"
# base_url ="http://www.meipai.com/media/444001066"
# data = urlparse.urlsplit(url, scheme='')
	data = urlparse.urlparse(url)
	objectpath = str(data.path)
	items =  objectpath.split("/")
	objectItem = ""
	for item in items:
		if(len(item) > 10):
			objectItem = item
	print objectItem
	base_url = base.replace("{1}", objectItem)
	import sys  
	reload(sys)  
	sys.setdefaultencoding('utf8')   
	request = urllib2.Request(base_url)
	response = urllib2.urlopen(request, data=None)
# print response.read()
	reader = response.read()
	print reader

	str_json = json.loads(reader)
	result = str_json.get("result")
	item = result[0]
	str_item = item.get("scheme")+item.get("host")+item.get("path")
	print str_item
	return str(str_item)

if __name__=="__main__":
	url = "http://m.miaopai.com/show/channel/HYTXfJLr~gc9YgQm2kGiNQ__"
	getMiaoPai(url)
	pass