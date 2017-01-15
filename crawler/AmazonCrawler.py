# -*- coding: UTF-8 -*-

# from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from urls import urls

import datetime
import time
import re
import json
import urllib2
import socket
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
timeout = 99999999
socket.setdefaulttimeout(timeout)

class AmazonCrawler:
    def __init__(self):
        cap = webdriver.DesiredCapabilities.PHANTOMJS
        cap["phantomjs.page.settings.resourceTimeout"] = 1000
        cap["phantomjs.page.settings.loadImages"] = False
        cap["phantomjs.page.settings.localToRemoteUrlAccessEnabled"] = True
        cap["userAgent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0"
        cap["XSSAuditingEnabled"] = True
        self.driver = webdriver.PhantomJS(desired_capabilities=cap,
                                      service_args=['--ignore-ssl-errors=true',
                                                    '--ssl-protocol=any',
                                                    '--web-security=true'
                                                    ])
        # self.driver = webdriver.Chrome()
        self.start()

    def start(self):
        result = []
        for i in urls:
            websites = urls[i]
            total_comment = 0
            for url in websites:
                comment = self.get_comment(url)
                total_comment += comment
            today = datetime.datetime.now().strftime('%Y-%m-%d')
            temp = {'commodity': 'insta360 Nano', 'country': i, 'comment_count': total_comment,'site': 'amazon', 'date': today}
            print temp
            result.append(temp)
        self.driver.quit()
        jsonResult = json.dumps(result)
        return jsonResult


    def get_comment(self ,url):
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 20)
        try:
            temp = wait.until(lambda x: x.find_element_by_id("acrCustomerReviewText").text)
            print temp
            pattern = re.compile('\d+', re.S)
            items = re.findall(pattern, temp)
            temp = items[0]
            comment_count = int(temp)
        except TimeoutException:
            comment_count = 0
            print url
        return comment_count


if __name__ == "__main__":
    amazon = AmazonCrawler()
