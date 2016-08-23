# coding:utf-8
"""
cloect newrand with newrand api
"""
import md5
import requests
import uuid
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def new_rand():
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
    print len(item)
    import time
    old_time = time.time() - (60 * 60 * 24 * 2)
    print time.strftime('%Y-%m-%d', time.localtime(old_time))

src = md5.new()
nonce = "e895b0aa6"


import calendar
import time


def _get_month_and_year():
    year = time.strftime('%Y', time.localtime(time.time()))
    month = time.strftime('%m', time.localtime(time.time()))
    print year, month
    return year, month


def _del_rule(end_time, start_time, rank_name, rank_name_group, nonce, chice_day_week_month):
    src.update(
        "/xdnphb/list/{0}/rank?AppKey=joker&end={1}&rank_name={3}&rank_name_group={4}&start={2}&nonce={5}".format(
            chice_day_week_month, end_time, start_time, rank_name, rank_name_group, nonce))
    data = {
        "end": "%s" % end_time,
        "rank_name": "%s" % rank_name,
        "rank_name_group": "%s" % rank_name_group,
        "start": "%s" % start_time,
        "nonce": nonce,
        "xyz": src.hexdigest()
    }
    print data
    return data


def _get_nonce():
    nonce = uuid.uuid4().hex[0:9]
    return nonce


def _del_rule_day(end_time, start_time, rank_name, rank_name_group, nonce):
    return _del_rule(end_time, start_time,
                     rank_name, rank_name_group, nonce, "day")


def _del_rule_week(end_time, start_time, rank_name, rank_name_group, nonce):
    return _del_rule(end_time, start_time,
                     rank_name, rank_name_group, nonce, "week")


def _del_rule_month(end_time, start_time, rank_name, rank_name_group, nonce):
    return _del_rule(end_time, start_time,
                     rank_name, rank_name_group, nonce, "month")


def _last_month_start_end():
    """
    获得上个月的第一天和最后一天
    """
    now_month = time.strftime('%m', time.localtime(time.time()))
    year = time.strftime('%Y', time.localtime(time.time()))
    d = calendar.monthrange(int(year), int(now_month))[1]
    last_time = 3600 * 24 * d
    last_month_time = time.time() - last_time
    month = time.strftime('%m', time.localtime(last_month_time))
    year = time.strftime('%Y', time.localtime(last_month_time))
    print year, month
    d = calendar.monthrange(int(year), int(month))
    return "%s-%s-01" % (year, month), "%s-%s-%s" % (year, month, d[1])


def _get_header():
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
    return headers


def _get_base_url(chice_day_week_month):
    base_url = "http://www.newrank.cn/xdnphb/list/{0}/rank".format(
        chice_day_week_month)
    return base_url


import datetime


def _get_last_week_start_end():
    """ 获取 一周start_time and end_time"""
    lastFriday = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    while lastFriday.weekday() != calendar.SUNDAY:
        lastFriday -= oneday
    print lastFriday
    sunday = lastFriday
    # sunday = lastFriday.strftime('%d')
    while lastFriday.weekday() != calendar.MONDAY:
        lastFriday -= oneday
    print lastFriday
    # monday = lastFriday.strftime('%d')
    monday = lastFriday
    print sunday, monday
    # print str(sunday), str(monday)
    return str(monday), str(sunday)


def _last_day_start_end():
    """ 获取昨天 """
    old_time = time.time() - (60 * 60 * 24 * 1.5)
    old = time.strftime('%Y-%m-%d', time.localtime(old_time))
    return old, old


def _get_item(url, data):
    try:
        r = requests.post(url, headers=_get_header(), data=data)
        items = (r.json().get("value"))
        return items
    except Exception as e:
        print e
        return []


def _last_week(rank_name, rank_name_group):
    start_time, end_time = _get_last_week_start_end()
    nonce = _get_nonce()
    # nonce = "36498448b"
    data = _del_rule_week(end_time, start_time,
                          rank_name, rank_name_group, nonce)
    r = requests.post(_get_base_url("week"), headers=_get_header(), data=data)
    # print r.content
    # print dir(r)
    items = (r.json().get("value"))
    for item in items:
        print item.get("biz_info"), item.get("account"), item.get("name")


def _last_month(rank_name, rank_name_group):
    start_time, end_time = _last_month_start_end()
    nonce = _get_nonce()
    # nonce = "e895b0aa6"
    data = _del_rule_month(end_time, start_time,
                           rank_name, rank_name_group, nonce)
    print data
    r = requests.post(_get_base_url("month"), headers=_get_header(), data=data)
    items = (r.json().get("value"))
    for item in items:
        print item.get("biz_info"), item.get("account"), item.get("name")


def _last_day(rank_name, rank_name_group):
    start_time, end_time = _last_day_start_end()
    nonce = _get_nonce()
    data = _del_rule_day(end_time, start_time,
                         rank_name, rank_name_group, nonce)
    url = _get_base_url("day")
    items = _get_item(url, data)
    for item in items:
        print item.get("biz_info"), item.get("account"), item.get("name")

_last_day("民生", "资讯")
# _last_month("民生", "资讯")
# _get_last_week_start_end()
# _get_month_and_year()
# _del_rule("2016-07-31", "2016-07-01", "民生", "资讯", "e895b0aa6", "month")
old_time = time.time() - (60 * 60 * 24 * 1.5)
old = time.strftime('%Y-%m-%d', time.localtime(old_time))
print old
