# coding:utf-8
import requests
from bs4 import BeautifulSoup
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "SINAGLOBAL=5519573560450.226.1439213791389; __utma=182865017.296035900.1457452995.1457452995.1457452995.1; __utmz=182865017.1457452995.1.1.utmcsr=verified.weibo.com|utmccn=(referral)|utmcmd=referral|utmcct=/verify/personalverify; wb_bub_hot_3621185105=1; TC-Ugrow-G0=5e22903358df63c5e3fd2c757419b456; SSOLoginState=1467360749; TC-V5-G0=40eeee30be4a1418bde327baf365fcc0; _s_tentry=login.sina.com.cn; Apache=8098963642982.408.1467360757489; ULV=1467360757500:38:1:1:8098963642982.408.1467360757489:1465397322685; TC-Page-G0=6fdca7ba258605061f331acb73120318; wb_g_minivideo_3621185105=1; YF-Ugrow-G0=9642b0b34b4c0d569ed7a372f8823a8e; YF-V5-G0=d22a701aae075ca04c11f0ef68835839; YF-Page-G0=7b9ec0e98d1ec5668c6906382e96b5db; WBStore=8ca40a3ef06ad7b2|undefined; wvr=6; UOR=,,login.sina.com.cn; SCF=AtY9j62XYdKgC_bZZPUwKzvTGbRIg8f_NTLycD4ee6LYl_kCwxMHUzfUBkRNzec18PhYbN_DR28vkmkHN1Ti7Rs.; SUB=_2A256gz2cDeTxGeVI6VMQ-CvNyzmIHXVZ-ShUrDV8PUNbmtAKLU3AkW8bkwKPt2C-2eeLIHOA3SOcvsdkqg..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whe.pn2WC3aa0iK5ZDOMSK15JpX5K2hUgL.Foeceo2p1h-peh-2dJLoI79-BLUi-Xjt; SUHB=05i6hx4GA33uOk; ALF=1500021068; un=15920329700",
    "Host": "weibo.com",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": 1,
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}
url = "http://weibo.com/206476669?profile_ftype=1&is_all=1#_0"
r = requests.get(url, headers=headers)
soup = BeautifulSoup((str(r.content)).replace("\\", ""), "lxml")
print soup
items = soup.find_all("div", attrs={"node-type": "feed_content"})
print items
print len(items)
