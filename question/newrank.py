# coding:utf-8
from selenium import webdriver
import requests
import time
print "begin"
firfox = webdriver.Firefox()

url = "http://www.newrank.cn/public/info/list.html"
# r = requests.get(url)
# print r.content
print "start"
import sys

reload(sys)
sys.setdefaultencoding('utf8')
firfox.get(url)
# firfox.wait
time.sleep(5)
print firfox.page_source
# firfox.close()
