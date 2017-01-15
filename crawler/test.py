# -*- coding: UTF-8 -*-
from urls import *
import requests
import datetime
import json
import re
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

url = 'https://www.amazon.de/Insta360-Nano-hardwrk-Kamera-zertifiziert/dp/B01M09S1AS/ref=sr_1_1?ie=UTF8&qid=1482249287&sr=8-1&keywords=insta360'

#
# if 'the first to review this item' in content:
#     sales = 0
# else:
#     pattern = re.compile('\d+ customer reviews</span>', re.S)
#     items = re.findall(pattern, content)
#     sales = (int)(items[0][:-24])
# print sales

def get_comment(url, country):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
        # 'Host': 'www.amazon.in',
        'Upgrade-Insecure-Requests': '1'
    }
    # try:
    page = requests.get(url, headers=headers)
    # except:
    #     print 'error'
    #     return 0
    content = page.text.encode('utf-8')
    print content
    if first[country] in content:
        print 0
        return 0
    pattern = re.compile('\d+' + ' Kundenrezensionen</a>', re.S)
    items = re.findall(pattern, content)
    temp = items[0]
    pattern = re.compile('\d+', re.S)
    items = re.findall(pattern, temp)
    sales = (int)(items[0])
    print sales
    return sales

import ssl
from functools import wraps

def sslwrap(func):
    @wraps(func)
    def bar(*args, **kw):
        kw['ssl_version'] = ssl.PROTOCOL_TLSv1
        return func(*args, **kw)
    return bar
ssl.wrap_socket = sslwrap(ssl.wrap_socket)
get_comment(url, '德国')