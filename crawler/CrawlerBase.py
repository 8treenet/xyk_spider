__author__ = 'ys'

import time
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from lxml import etree

class CrawlerBase:
    _url = ''
    _html = None
    _driver = None
    def __init__(self, *args, **kwargs):
        return
    def request(self, url, autoClose = True,loadImages = False, cookie='', reconnectCount = 3, timeSleep = 1.5, delayTime = 0.5):
        time.sleep(delayTime)
        cap = webdriver.DesiredCapabilities.PHANTOMJS
        cap['browserName'] = 'Mozilla/5.0'
        cap['platform'] = 'Linux'
        cap['phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        cap["phantomjs.page.customHeaders.Cookie"] = cookie
        cap['phantomjs.page.settings.loadImages'] = loadImages
        driver = webdriver.PhantomJS()
        driver.set_window_size(1280, 800)
        driver.get(url)


        time.sleep(timeSleep)
        self._url = driver.current_url
        self._html = etree.HTML(driver.page_source)
        if autoClose:
            driver.quit()
        else:
            self._driver = driver
        self.response()
        return driver

    def response(self, driver):
        return

    def getUrl(self):
        return self._url