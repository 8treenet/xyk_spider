#coding:utf-8
__author__ = 'ys'

from selenium.webdriver.common.by import By
from CrawlerBase import CrawlerBase
from lxml import etree
import re
import urllib
import time
import os
import hashlib
import datetime
import urlparse


class SpdbCrawler(CrawlerBase):
    urlList = ['http://ccc.spdb.com.cn/news/qgxhd/','http://ccc.spdb.com.cn/news/qyxhd/','http://ccc.spdb.com.cn/news/jwyhhd/','http://ccc.spdb.com.cn/news/sqjtjhd/']
    url = 'http://ccc.spdb.com.cn/news/qyxhd/'
    bank_id  = 4
    def __init__(self, *args, **kwargs):
        CrawlerBase.__init__(self, *args, **kwargs)

    def response(self):
        return

    #返回基本信息
    def get(self):
        result = []
        time.sleep(1)
        button = self._driver.find_element_by_xpath(u'//a[@class="rowceil" and text() = "活动进行中"]')
        button.click()

        while True:
            time.sleep(2)
            result.extend(self.getList())
            if not self.next():
                break

        self._driver.quit()
        return result

    #下一页有返回真并且跳转
    def next(self):
        #解析当前页面是否可以跳转
        try:
            page = self._driver.find_element_by_xpath(u'//*[@class="classPage" and text() = "下一页"]')
            page.click()
            return True
        except:
            return False

    #返回本页数据
    def getList(self):
        result = []
        html = etree.HTML(self._driver.page_source)
        list = html.xpath('//div[@class="newsright_news"]')
        for item in list:
            a  = item.xpath('a')
            if len(a) <= 0:
                continue
            a = a[0]
            url = a.xpath('@href')
            name = a.xpath('div[2]/text()')
            date = a.xpath('div[3]/text()')

            info = {}
            info['name'] = len(name) > 0 and name[0] or ''
            info['date'] = len(date) > 0 and date[0] or ''
            info['url'] = len(url) > 0 and url[0] or ''
            info['beginDate'] = info['date']
            info['endDate'] = ''
            result.append(info)
        return result