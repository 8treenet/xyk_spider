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

#广发银行
class CgbCrawler(CrawlerBase):
    urlList = ['http://card.cgbchina.com.cn/Channel/11820301','http://card.cgbchina.com.cn/Channel/11820220','http://card.cgbchina.com.cn/Channel/11820139','http://card.cgbchina.com.cn/Channel/15679698']
    url = 'http://card.cgbchina.com.cn/Channel/11820301'
    bank_id  = 7
    def __init__(self, *args, **kwargs):
        CrawlerBase.__init__(self, *args, **kwargs)

    def response(self):
        return

    #返回基本信息
    def get(self):
        result = []
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
            pages = self._driver.find_elements_by_xpath('//*[@id="subForm"]/div/span/a')
            for page in pages:
                if page.text.find(u'下一页') >= 0:
                    page.click()
                    return True
        except:
            return False

    #返回本页数据
    def getList(self):
        result = []
        html = etree.HTML(self._driver.page_source)
        list = html.xpath('//*[@class="youhui_content"]/ul')
        for item in list:
            li  = item.xpath('li')
            if len(li) <= 0:
                continue
            li = li[0]
            url = li.xpath('h3/a/@href')
            name = li.xpath('h3/a/text()')
            date = li.xpath('p/text()')

            info = {}
            info['name'] = len(name) > 0 and name[0] or ''
            info['name'] = info['name'].strip()
            info['date'] = len(date) > 0 and date[0] or ''
            info['url'] = len(url) > 0 and url[0] or ''
            info['beginDate'] = info['date']
            info['endDate'] = ''
            if info['url'].find('http://') < 0:
                info['url'] = 'http://card.cgbchina.com.cn' + info['url']
            result.append(info)
        return result