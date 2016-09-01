# coding:utf-8
import requests
import re
import time
import datetime
import urlparse
import calendar
import random

import sys
reload(sys)
sys.setdefaultencoding('utf8')


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
    # print js
    status = js.get('status')
    if status == 'OK':
        items = js.get("result").get("items")
        # print items
        if items:
            item = items[0]
            if item:
                url = item.get("url")
                print url
                scheme = urlparse.urlparse(url)
                parse_qs = urlparse.parse_qs(scheme.query)
                bizs = parse_qs['__biz']
                if bizs:
                    biz = bizs[0]
                    print biz
                    return biz
    return None


# get_recommendArticles(104683)


def _last_day_start_end():
    """ 获取昨天 """
    old_time = time.time() - (60 * 60 * 24 * 2)
    old = time.strftime('%Y-%m-%d', time.localtime(old_time))
    return old


def _get_last_week_start_end():
    """ 获取 一周start_time and end_time"""
    lastFriday = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    while lastFriday.weekday() != calendar.SATURDAY:
        lastFriday -= oneday
    # print lastFriday
    sunday = lastFriday
    # sunday = lastFriday.strftime('%d')
    while lastFriday.weekday() != calendar.SUNDAY:
        lastFriday -= oneday
    # print lastFriday
    # monday = lastFriday.strftime('%d')
    monday = lastFriday
    # print sunday, monday
    # print str(sunday), str(monday)
    return str(sunday).replace("-", "") + "_" + str(monday).replace("-", "")


def _last_month_start_end():
    """
    获得上个月的第一天和最后一天
    """
    now_month = time.strftime('%m', time.localtime(time.time()))
    year = time.strftime('%Y', time.localtime(time.time()))
    d = calendar.monthrange(int(year), int(now_month))[1]
    last_time = 3600 * 24 * d
    last_month_time = time.time() - last_time - last_time
    month = time.strftime('%m', time.localtime(last_month_time))
    year = time.strftime('%Y', time.localtime(last_month_time))
    print year, month
    d = calendar.monthrange(int(year), int(month))
    return "%s-%s-%s" % (year, month, d[1]) + "_" + "%s-%s-01" % (year, month)
# print _get_last_week_start_end()
# print _last_month_start_end()


def getwxrands(gid, date, page, _type):
    t = str(random.random()) + str(random.randint(1001, 9999))
    url = "http://www.gsdata.cn/newRank/getwxranks?gid={0}&date={1}&page={2}&type={3}&cp=all&t={4}&action=".format(
        gid, date, page, _type, t)
    print "url = ", url
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
        # "Cookie": "PHPSESSID=fo7r7e91ncjla52qkjv04m5mn0",
        "Referer": "http://www.gsdata.cn/rank/detail",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    r = requests.get(url, headers=headers)
    jstr = r.json()
    print jstr
    error = jstr.get('error')
    if error == 0:
        data = jstr.get("data")
        rows = data.get("rows")
        return rows
    return []
    # for row in rows:
    #     nickname_id = row.get('nickname_id')
    #     wx_nickname = row.get('wx_nickname')
    #     wx_name = row.get('wx_name')
    #     o_nickname_id = row.get('o_nickname_id')
    #     print nickname_id, wx_nickname, wx_name, o_nickname_id


# getwxrands()


def table():
    data = {"4269": "报纸", "37": "期刊", "12591": "广播", "14493": "视频",
            "7684": "电视", "24512": "时政", "11671": "门户网站", "25003": "传媒观察",
            "62": "自媒体", "4484": "医疗", "4482": "美容", "4278": "鞋服",
            "547": "休娱", "4275": "酒店", "4271": "餐饮", "32570": "游艇",
            "205": "汽车", "4280": "家居", "9800": "电器", "8527": "手机",
            "551": "珍奢", "32567": "珠宝", "32565": "黄金", "9931": "银行",
            "12589": "保险", "26480": "股市", "26624": "财会", "21294": "P2P",
            "12209": "电商", "30227": "快消", "201": "房地产", "26482": "企业",
            "26377": "企业家", "15658": "航空公司", "44041": "运营商", "5031": "销售管理",
            "192": "健康", "4485": "运动", "28082": "篮球", "27502": "足球", "30174": "跑步",
            "28226": "高尔夫", "30221": "茶类", "30223": "收藏", "4486": "宗教",
            "7567": "历史", "42": "科技", "193": "时尚", "43": "文化", "29506": "读",
            "530": "视觉", "197": "幽默", "198": "情感", "26488": "亲子",
            "26392": "社群", "4757": "生活服务", "10612": "明星", "18167": "公益",
            "542": "职场", "13797": "游戏", "16520": "酒吧", "41093": "二次元",
            "46454": "排行榜", "26975": "航空", "27299": "铁路", "27298": "公交",
            "27382": "地铁", "196": "旅行", "359": "军事", "4483": "农业",
            "4277": "法律", "13795": "物流", "4267": "财经", "13812": "石化",
            "13810": "建筑", "12777": "环境", "242": "大数据", "12778": "出版",
            "12480": "学术", "199": "教育", "46": "大学", "26813": "中学",
            "26684": "小学", "26917": "幼儿园", "10755": "图书馆", "43176": "无人机",
            "45577": "博物馆", "43201": "VR", "4445": "政府", "4443": "党建",
            "1009": "宣传", "4444": "团委", "4446": "公安", "4447": "司法",
            "4448": "纪检", "12779": "工商", "4449": "税务", "5576": "文教",
            "11142": "环保", "12780": "交通", "48": "旅游", "4450": "气象",
            "12506": "人社", "13553": "卫生", "30626": "工会", "41078": "检察",
            "41091": "法院", "45826": "食药监", "43699": "省妇联",
            "43700": "市妇联", "46479": "政法", "46835": "安监", "4477":
            "其他", "369": "北京", "388": "上海", "394": "天津", "586": "重庆",
            "391": "广东", "587": "江苏", "588": "浙江", "589": "安徽", "590": "福建",
            "591": "山东", "593": "河北", "594": "山西", "595": "内蒙古", "596": "辽宁",
            "613": "吉林", "614": "黑龙江", "617": "河南", "618": "湖北", "621": "湖南",
            "623": "广西", "626": "四川", "629": "贵州", "630": "云南", "632": "西藏",
            "635": "陕西", "649": "甘肃", "651": "青海", "652": "宁夏", "653": "新疆",
            "1268": "江西", "1675": "海南", "402": "港澳台", "654": "海外"}
    return data


def choice():
    data = table()
    keys = data.keys()
    for key in keys:
        print key, data.get(key)
        time.sleep(1)
        getwxrands(key, _last_day_start_end(), 2, "day")
        break


def _one_day(gid, page):
    return getwxrands(gid, _last_day_start_end(), page, "day")


def _one_week(gid, page):
    return getwxrands(gid, _get_last_week_start_end(), page, "week")


def _one_month(gid, page):
    return getwxrands(gid, _last_month_start_end(), page, "month")


def _save_wx(nickname_id, wx_nickname, wx_name, o_nickname_id):
    pass


def get_():
    data = table()
    keys = data.keys()
    for key in keys:
        print key, data.get(key)
        time.sleep(1)
        rows = _one_month(key, 1)
        for row in rows:
            nickname_id = row.get('nickname_id')
            wx_nickname = row.get('wx_nickname')
            wx_name = row.get('wx_name')
            o_nickname_id = row.get('o_nickname_id')
            print nickname_id, wx_nickname, wx_name, o_nickname_id
        break

get_()


def get_detail():
    pass
