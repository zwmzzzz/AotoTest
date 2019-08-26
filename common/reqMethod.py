# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 13:51
# @Author  : wenming.zhao
# @Email   : zwm2007@163.com
# @File    : reqMethod.py
# @Software:
import os

import configparser

import requests

base_path=str(os.path.dirname(os.path.dirname(__file__)))
base_path=base_path.replace('\\','/')
cfg_path=base_path+'/config.ini'

cf=configparser.ConfigParser()
cf.read(cfg_path,encoding='utf-8')
host=cf.get('URL','base_url')

class RequestMethod:
    def __init__(self):
        self.base_url=cf.get('URL','base_url')
        self.data={}
        self.files={}
    def get(self,url,params):
        test_url=self.base_url + url
        try:
            return requests.get(url=test_url,params=params,timeout=16)
        except TimeoutError:
            return print('%s get request timeout!' %url)

    def post(self, url, **kwargs):
        url=self.base_url+url
        params=kwargs.get('params')
        data=kwargs.get('data')
        json=kwargs.get('json')
        try:
            print('url:',url)
            print("params",params)
            result2=requests.post(url,params=params,data=data,json=json)
            return result2
        except Exception as e:
            return print('%s post request timeout!' % url)


if __name__=='__main__':
    a=RequestMethod()
    print(a.get(url='get',params=''))

