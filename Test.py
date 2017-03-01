#coding:utf-8
__author__ = 'ys'
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from redis import Redis
from public.Config import *
from Master import *
from Worker import *
import MySQLdb
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import requests
import json
from crawler.WeiMengCrawler import *

#启动测试 请关闭master和worker中的main_master()和main_worker
def main():
    cache = Redis(host=redis_address, port=6379, db=0, password=redis_password)
    cache.delete('spider_shop_new')
    cache.rpush('spider_shop_new', 136102887)
    thread.start_new_thread(thread_download, ())
    while True:
        print 'a'
# try:
#     main()
# except:
#     pass
