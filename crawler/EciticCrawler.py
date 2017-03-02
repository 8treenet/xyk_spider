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


class EciticCrawler(CrawlerBase):
    url = 'http://creditcard.ecitic.com/youhui/shuakahuodong.shtml'
    bank_id  = 1
    def __init__(self, *args, **kwargs):
        CrawlerBase.__init__(self, *args, **kwargs)

    def response(self):
        return

     #返回基本信息
    def get(self):
        result = []
        html = self._html
        List = html.xpath('//*[@class="yhhd_list_right"]')
        for item in List:
            info = {}
            name = item.xpath('p[@class="yhhd_list_tit"]/text()')
            date = item.xpath('p[@class="yhhd_list_date"]/text()')
            url  = item.xpath('a/@href')

            if len(name) > 0 :
                name = name[0]
            else:
                name = ''

            if len(date) > 0 :
                date = date[0]
            else:
                date = ''

            if len(url) > 0 :
                url = url[0]
                if url.find('http://') < 0:
                    url = 'http://creditcard.ecitic.com' + url
            else:
                url = ''

            info['name'] = name
            info['date'] = date
            info['url'] = url
            info['beginDate'] = ''
            info['endDate'] = ''

            if date:
                dateList = date.split('-')
                if len(dateList) > 1:
                    info['endDate'] = dateList[1].replace('/', '-')
                    beginDate = dateList[0].split('：')
                    if len(beginDate) > 1:
                        info['beginDate'] = beginDate[1].replace('/', '-')
            result.append(info)

        return result