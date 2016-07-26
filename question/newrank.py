# coding:utf-8
from selenium import webdriver
import sys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

reload(sys)
sys.setdefaultencoding('utf8')
print "begin"
print dir(webdriver)

user_agent = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) " +
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
)
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = user_agent

# firfox = webdriver.PhantomJS(desired_capabilities=dcap)

firfox = webdriver.Firefox()

url = "http://www.newrank.cn/public/info/list.html"
# print "start"
# firfox.maximize_window()
firfox.get(url)
time.sleep(15)


def action(browser, item):
    # print item.parent
    # print type(item.parent)
    # print type(item)
    # ActionChains(browser).move_to_element(item).perform()
    # ActionChains(browser).click(item).perform()
    # item.click()
    pass


def runjs():
    pass


def pprint(num, item, browser):
    print num
    if item:
        # print item.text
        time.sleep(3)
        print dir(item)
        browser.save_screenshot("./%s.png" % num)
        action(browser, item)
        print item.text
        item.click()
        time.sleep(10)
        # print browser.page_source
        # item.click()
    print "=========="
# top = firfox.find_element_by_xpath(
    # "//div[@id='rank_main']/div[@id='rank_data']/div[@class='left_menu']/div[@class='life']")


def moveTop(browser):
    # global top
    # ActionChains(browser).move_to_element(top).perform()
    # js = "function simulate(f,c,d,e){var b,a=null;for(b in eventMatchers)if(eventMatchers[b].test(c)){a=b;break}if(!a)return!1;document.createEvent?(b=document.createEvent(a),a==\"HTMLEvents\"?b.initEvent(c,!0,!0):b.initMouseEvent(c,!0,!0,document.defaultView,0,d,e,d,e,!1,!1,!1,!1,0,null),f.dispatchEvent(b)):(a=document.createEventObject(),a.detail=0,a.screenX=d,a.screenY=e,a.clientX=d,a.clientY=e,a.ctrlKey=!1,a.altKey=!1,a.shiftKey=!1,a.metaKey=!1,a.button=1,f.fireEvent(\"on\"+c,a));return!0} var eventMatchers={HTMLEvents:/^(?:load|unload|abort|error|select|change|submit|reset|focus|blur|resize|scroll)$/,MouseEvents:/^(?:click|dblclick|mouse(?:down|up|over|move|out))$/}; " + \
    # "simulate(arguments[0],\"mousedown\",0,0); simulate(arguments[0],\"mousemove\",arguments[1],arguments[2]); simulate(arguments[0],\"mouseup\",arguments[1],arguments[2]); ",
    # print browser.execute_script(js, 100, 100)
    print browser.execute_script("document.title")

try:
    firfox.execute_script(
        'document.getElementById("header").style.display="none";document.getElementsByClassName("l_nav")[0].style.display="none";document.getElementsByClassName("l_date")[0].style.display="none";document.getElementsByClassName("header-search-inner")[0].style.display="none";document.getElementsByClassName("new-header")[0].style.display="none";document.getElementsByClassName("new_tab")[0].style.display="none";document.getElementById("header-search").style.display="none";')
    items = firfox.find_element_by_xpath(
        "//div[@id='rank_main']/div[@id='rank_data']/div[@class='left_menu']/div[@class='zixun']/ul[@id='day_zixun_links']/li[2]")
    pprint(1, items, firfox)

    # item = firfox.find_element_by_xpath(
    # "//div[@id='rank_main']/div[@id='rank_data']/div[@class='left_menu']/div[@class='zixun']")
    # pprint(2, item)
    item = firfox.find_element_by_xpath(
        "//div[@id='rank_main']/div[@id='rank_data']/div[@class='left_menu']/div[@class='life']")
    pprint(3, item, firfox)
    items = firfox.find_element_by_xpath(
        "//div[@id='rank_main']/div[@id='rank_data']/div[@class='left_menu']/div[@class='life']/ul[@id='day_life_links']/li[2]")
    moveTop(firfox)
    pprint(4, items, firfox)
# firfox.find_elements_

    firfox.close()
except Exception as e:
    print "error"
    print e
    firfox.close()
