#coding:utf-8
__author__ = 'ys'

from selenium.webdriver.common.by import By
from CrawlerBase import CrawlerBase
import re
import urllib
import time
import os
import hashlib
import datetime
import urlparse


class CibCrawler(CrawlerBase):
    urlList = ['http://creditcard.cib.com.cn/promotion/national', 'http://creditcard.cib.com.cn/promotion/overseas/HKMacau',
               'http://creditcard.cib.com.cn/promotion/overseas/sales','http://creditcard.cib.com.cn/promotion/area']
    url = 'http://creditcard.cib.com.cn/promotion/national'
    bank_id  = 6
    def __init__(self, *args, **kwargs):
        CrawlerBase.__init__(self, *args, **kwargs)

    def response(self):
        return

     #返回基本信息
    def get(self):
        result = []
        Next = True
        while Next:
            html = self._html
            lis = html.xpath('//*[@id="main"]/ul/li')
            for li in lis:
                info = {}
                date = li.xpath('span/text()')
                name = li.xpath('a/text()')
                url  = li.xpath('a/@href')
                info['name'] = len(name) > 0 and name[0] or ''
                info['date'] = len(date) > 0 and date[0] or ''
                info['url'] = len(url) > 0 and url[0] or ''
                info['beginDate'] = info['date']
                info['endDate'] = ''

                if info['url'].find('http://') < 0:
                    info['url'] = 'http://creditcard.cib.com.cn' + info['url']
                result.append(info)

            alist = html.xpath('//*[@id="main"]/div[@class="page_arw"]/a')
            Next = False
            for a in alist:
                nexta = a.xpath('img[@src="/resources/images/2012/arrow-right.gif"]')
                if len(nexta) > 0:
                    href = a.xpath('@href')
                    if len(href) > 0:
                        self.request('http://creditcard.cib.com.cn/' + href[0])
                        Next = True
                        time.sleep(2)

        return result