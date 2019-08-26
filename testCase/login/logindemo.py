# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 17:15
# @Author  : wenming.zhao
# @Email   : zwm2007@163.com
# @File    : login.py
# @Software: PyCharm
import unittest

import ddt

from common.getParams import get_req_params
from common.reqMethod import RequestMethod
test_data = [{
    "clientCode": "韩",
    "topic": "测试接口",
    "content": "测试接口",
    "resrcType": "0",
    "assert": "200"
},
    {
        "clientCode": "",
        "topic": "测试接口2",
        "content": "测试接口2",
        "resrcType": "0",
        "assert": "400"
    },
    {
        "clientCode": "韩",
        "topic": "",
        "content": "测试接口2",
        "resrcType": "0",
        "assert": "400"
    }]

@ddt.ddt
class Login(unittest.TestCase):
    def setUp(self):
        self.url='post'
        self.sheet='login'

    def tearDown(self):
        pass

    @ddt.data(*test_data)
    def test_log_success(self,par):
        case='test_login_success'
        #param=get_req_params(self.sheet,case)
        print('prar:',par)
        self.req_result=RequestMethod().post(self.url,params=par).text
        #c=self.req_result.json()
        #print(c)
        print('req_result:',self.req_result)
        self.assertEqual(self.req_result['origin'],'101.86.20.3, 101.86.20.3')


if __name__=='__main__':
    unittest.main()
    print(111)
    print(32222)