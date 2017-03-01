#coding:utf-8
__author__ = 'ys'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import thread
import json


from crawler.EciticCrawler import *
from model.XykSprider import *
import traceback

db = XykSprider()
ecitic = EciticCrawler()
ecitic.request(ecitic.url)
list = ecitic.get();
for item in list:
    if db.check(ecitic.bank_id, item['name'], item['url']):
        continue
    db.add(ecitic.bank_id, item['name'], item['date'], item['url'])