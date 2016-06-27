#coding:utf-8
"""
根据搜狗搜索微信公众号写的小工具，获取某微信号的页面信息
缺点是不完善，如果没有最新的消息不会到历史消息去找
"""
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


headers={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, sdch",
            "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
            "Cache-Control":"no-cache",
            "Connection":"keep-alive",
            "Host":"weixin.sogou.com",
            "Pragma":"no-cache",
            'Upgrade-Insecure-Requests':1,
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
}
proxies ={
    "http":"202.75.210.45:7777"
}
print "start"
base_url = "http://weixin.sogou.com/weixin?type=1&query={0}&ie=utf8&_sug_=n&_sug_type_="
def sogou(url):
    r = requests.get(base_url,headers=headers)
    soup = BeautifulSoup(r.content,"lxml")
    all = soup.find_all("div",attrs={'class':'txt-box'})
    for item in all:
        print "=======-----======"
        print item.find_all("h3")[0].text
        print item.find_all("h4")[0].find_all('label')[0].text
        sp_txt = item.find_all("span",attrs={'class':'sp-txt'})
        if sp_txt:
            if len(sp_txt) == 2:
                a_all = sp_txt[1].find_all("a")
                if a_all:
                    a = a_all[0]
            # print dir(a)
                    print str(a.attrs['href']).replace(';','&')

base_url = base_url.format("girl")
print base_url
sogou(base_url)