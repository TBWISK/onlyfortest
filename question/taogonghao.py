# coding:utf-8
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def _get_header():
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "www.taogonghao.com",
        "Origin": "http://www.taogonghao.com",
        "Pragma": "no-cache",
        "Referer": "http://www.taogonghao.com/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    return headers


url = "http://www.taogonghao.com/wemedia.html?&page=2"

r = requests.get(url, headers=_get_header())
# print r.content
soap = BeautifulSoup(r.content, "lxml")
trs = soap.find_all("tr")
tr_indx = 0
for tr in trs:
    # print tr
    print "=========="
    # divs = tr.find_all("div", attrs={"class": "fl wz_name"})
    # if divs:
    # print divs[0]
    # divs = tr.find_all_previous("div", attrs={"class": "wx"})
    # if divs:
    # print divs[0].text
    if tr_indx == 0:
        tr_indx += 1
        continue
    tds = tr.find_all("td")

    if tds:
        name_weixin = tds[1].text
        av_read = tds[2].text
        funs = tds[3].text
        frist = tds[4].text
        second = tds[5].text
        tag = tds[6].text
        jiedan = tds[7].text
        credit = tds[8].text
        rate = tds[9].text
        print name_weixin, av_read, funs, funs, frist, second, tag, jiedan, credit, rate
        name_weixin = name_weixin.replace("扫描二维码关注", "").replace("\n", '')
        name_weixins = name_weixin.split(" ")
        print name_weixins[0], '---'
        print name_weixins[1], '---'

        # value = tds[11].text
    # idx = 0
    # for td in tds:

        # print idx, td.text
        # idx += 1
