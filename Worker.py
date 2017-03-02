#coding:utf-8
__author__ = 'ys'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import thread
import json


from crawler.EciticCrawler import *
from crawler.SpdbCrawler import *
from model.XykSpider import *
import traceback

db = XykSpider()
ecitic = EciticCrawler()
ecitic.request(ecitic.url)
list = ecitic.get();
for item in list:
    if db.check(ecitic.bank_id, item['name'], item['url']):
        continue
    db.add(ecitic.bank_id, item['name'], item['date'], item['url'], item['beginDate'], item['endDate'])



spdb = SpdbCrawler()
for url in spdb.urlList:
    spdb.request(url, False)
    list = spdb.get()
    for item in list:
        if db.check(spdb.bank_id, item['name'], item['url']):
            continue
        db.add(spdb.bank_id, item['name'], item['date'], item['url'], item['beginDate'], item['endDate'])