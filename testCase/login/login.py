# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 17:15
# @Author  : wenming.zhao
# @Email   : zwm2007@163.com
# @File    : login.py
# @Software: PyCharm
import unittest

from common.getParams import get_req_params
from common.reqMethod import RequestMethod


class Login(unittest.TestCase):
    def setUp(self):
        self.url='post'
        self.sheet='login'

    def tearDown(self):
        pass
    def test_log_success(self):
        case='test_login_success'
        param=get_req_params(self.sheet,case)
        print(param)
        self.req_result=RequestMethod().post(self.url,param=param).json()
        #c=self.req_result.json()
        #print(c)
        print(self.req_result)
        self.assertEqual(self.req_result['origin'],'101.86.20.3, 101.86.20.3')


if __name__=='__main__':
    Login.test_log_success()
    print()