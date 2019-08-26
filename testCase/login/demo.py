# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 16:14
# @Author  : wenming.zhao
# @Email   : zwm2007@163.com
# @File    : demo.py
# @Software: PyCharm


import requests
import json

host = "http://httpbin.org/"
endpoint = "post"

url = ''.join([host,endpoint])
params = {'key1':'params1','key2':'params2'}

# r = requests.post(url)
r = requests.post(url,params=params)
#response = r.json()
print (r.text)