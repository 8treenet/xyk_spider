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


class AgriculturalCrawler(CrawlerBase):
    urlList = [
        'http://www.95599.cn/cn/CreditCard/Special0ffers/skyhsxlb/?value=24&typeName=%E9%A4%90%E9%A5%AE%E7%BE%8E%E9%A3%9F',
        'http://www.95599.cn/cn/CreditCard/Special0ffers/skyhsxlb/?value=22&typeName=%E8%B6%85%E5%B8%82%E7%99%BE%E8%B4%A7',
        'http://www.95599.cn/cn/CreditCard/Special0ffers/skyhsxlb/?value=29&typeName=%E6%B1%BD%E8%BD%A6%E6%9C%8D%E5%8A%A1',
        'http://www.95599.cn/cn/CreditCard/Special0ffers/skyhsxlb/?value=25&typeName=%E5%87%BA%E8%A1%8C%E6%97%85%E6%B8%B8',
        'http://www.95599.cn/cn/CreditCard/Special0ffers/skyhsxlb/?value=23&typeName=%E7%94%9F%E6%B4%BB%E5%A8%B1%E4%B9%90',
        'http://www.95599.cn/cn/CreditCard/Special0ffers/skyhsxlb/?value=8&typeName=%E5%A2%83%E5%A4%96%E5%95%86%E6%88%B7',
        'http://www.95599.cn/cn/CreditCard/Special0ffers/skyhsxlb/?value=28&typeName=%E5%85%B6%E4%BB%96'
        ]
    url = 'http://www.95599.cn/cn/CreditCard/Special0ffers/skyhsxlb/?value=24&typeName=%E9%A4%90%E9%A5%AE%E7%BE%8E%E9%A3%9F'
    bank_id  = 5
    def __init__(self, *args, **kwargs):
        CrawlerBase.__init__(self, *args, **kwargs)

    def response(self):
        return

    #返回基本信息
    def get(self):
        result = []
        time.sleep(1)

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
            page = self._driver.find_element_by_xpath('//*[@class = "shez-lsjf_djya"]/font')
            page.click()
            return True
        except:
            return False

    #返回本页数据
    def getList(self):
        result = []
        html = etree.HTML(self._driver.page_source)
        list = html.xpath('//div[@class="widthPer100 fl"]')
        for item in list:
            a = item.xpath('p[1]/a')
            if len(a) <= 0:
                continue
            a = a[0]
            url = a.xpath('@href')
            name = a.xpath('text()')

            date = item.xpath('p[2]/span[2]/text()')

            info = {}
            info['name'] = len(name) > 0 and name[0] or ''
            info['date'] = len(date) > 0 and date[0] or ''
            info['url'] = len(url) > 0 and url[0] or ''
            info['beginDate'] = ''
            info['endDate'] = ''

            if info['url'].find('http://') < 0:
                info['url'] = 'http://www.95599.cn' + info['url']
            result.append(info)
        return result