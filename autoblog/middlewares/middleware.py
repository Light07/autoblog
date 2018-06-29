# -*- coding: utf-8 -*-
import os

from selenium import webdriver
from scrapy.http import HtmlResponse
import time

from autoblog.tools.log_processor import logger


class JavaScriptMiddleware(object):
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=self.options)

    def process_request(self, request, spider):
        if "zhihu.com" or "xueqiu.com" or "leiphone.com" in request.url:
            logger.info("chrome headless is starting...")
            self.driver.get(request.url)
            time.sleep(1)
            js = "window.scrollTo(0, document.body.scrollHeight);"
            self.driver.execute_script(js) #可执行js，模仿用户操作。此处为将页面拉至最底端。
            time.sleep(3)
            body = self.driver.page_source
            return HtmlResponse(self.driver.current_url, body=body, encoding='utf-8', request=request)
        else:
            return

    def spider_closed(self, spider, reason):
        os.system('taskkill /f /im chrome.exe')
        logger.info('close chrome driver......')