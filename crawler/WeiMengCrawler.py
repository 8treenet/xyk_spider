#coding:utf-8
__author__ = 'ys'

from selenium.webdriver.common.by import By
from CrawlerBase import CrawlerBase
import re
import urlparse
import time
import requests
import json


class WeiMengCrawler(CrawlerBase):

    def __init__(self, *args, **kwargs):
        CrawlerBase.__init__(self, *args, **kwargs)
    def response(self):
        return

    #返回cookie信息
    def getUser(self):
        user = {}
        if self._driver:
            self._driver.find_element_by_id('username').send_keys('3@57009414')
            self._driver.find_element_by_id('password').send_keys('123456')
            self._driver.find_element_by_id('login_button').click()
            time.sleep(3)
            self._driver.get('http://home.weimob.com/#/app/vip/55936473/tradeConsumeLog?page=1&count=20&PageIndex=1&PageSize=20')
            time.sleep(3)
            self._driver.save_screenshot('test.png')

            cookie = [item["name"] + "=" + item["value"] for item in self._driver.get_cookies()]
            user['cookie'] = '; '.join(item for item in cookie)

            for item in self._driver.get_cookies():
                if item["name"] == 'weimobAuthData':
                    user['weimobAuthData'] = item["value"]
                    break;
            self._driver.quit()
            return user
        return user

    def request(self, url):
        return CrawlerBase.request(self, url, autoClose = False)


# url = 'http://www.weimob.com/website/login.html'
# weimeng = WeiMengCrawler()
# driver = weimeng.request(url)
# user = weimeng.getUser()
#
# url = 'http://home.weimob.com/apiVip/GetConsumingLogPageListAndTotal'
# header = {
#     'Accept':'application/json, text/plain, */*',
#     'Accept-Encoding':'gzip, deflate',
#     'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
#     'Apiclient':'weimob-pc',
#     'Connection':'keep-alive',
#     'Content-Type':'application/json;charset=UTF-8',
#     'Cookie': user['cookie'],
#     'Host':'home.weimob.com',
#     'Origin':'http://home.weimob.com',
#     'Referer':'http://home.weimob.com/',
#     'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
#     'weimobAuthData':user['weimobAuthData']
# }
# jsonData = json.dumps({
# 'AId':'55936473',
# 'BeginTime':1483459200,
# 'EndTime':1483631999,
# 'PageIndex':1,
# 'PageSize':20,
# 'limit':20,
# 'page':1,
# 'page_num':1
# })
#
# response = requests.post(url, data=jsonData, headers=header)
# print response.text