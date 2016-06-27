#coding:utf-8
import requests
import re
from bs4 import BeautifulSoup
import jieba.analyse
# pip install jieba 
import json
base_url = "http://mp.weixin.qq.com/s?__biz=MzI0MDA4Mjc0Ng==&mid=2652248960&idx=1&sn=c9438dc5b3f319a69df1d344857ac399&scene=4#wechat_redirect"
r = requests.get(base_url)
# html='<a href="http://www.jb51.net">脚本之家</a>,Python学习！'
content = str(r.content)
r = BeautifulSoup(content,"lxml")
# print content
page_content = r.find_all('div',attrs={'id':'js_content'})
page =  page_content[0]
title = str(r.title)
new_page = title+str(page)
html_re = r'<[^>]+>'
dr = re.compile(html_re)
dd = dr.sub("",new_page)
print dd
analyse = jieba.analyse.extract_tags(dd,topK=30)
app = dict()
for item in range(len(analyse)):
    app.update({item:analyse[item].encode("utf-8")})
print app
js_str = json.dumps(app)
print js_str
ll = json.loads(js_str)
for item in ll:
    print ll[item].encode("utf-8")
# for item in app:
    # print app[item]

# print 



