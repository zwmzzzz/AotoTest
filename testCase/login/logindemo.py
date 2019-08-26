# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 17:15
# @Author  : wenming.zhao
# @Email   : zwm2007@163.com
# @File    : login.py
# @Software: PyCharm
import unittest

import ddt

from common.getParams import get_req_params
from common.readExcel import read_all_req
from common.reqMethod import RequestMethod
test_data = [{'account': '13000000000', 'password': '123456', 'system_type': '2', 'system_version': '1.0', 'device_uid': '87C4F987E5230C58A26E8A8A3E97A8CB', 'phone_model': 'iPad', 'role': '2', 'clientversion': '1.0.0', 'Response': '', 'code': '0', 'msg': '成功', 'user_name': '9705测试'}, {'account': '', 'password': '123456', 'system_type': '2', 'system_version': '1.0', 'device_uid': '87C4F987E5230C58A26E8A8A3E97A9CB', 'phone_model': 'iPad', 'role': '2', 'clientversion': '1.0.0', 'Response': '', 'code': '1', 'msg': '用户不存在', 'user_name': ''}, {'account': '13000000000', 'password': '111111', 'system_type': '2', 'system_version': '1.0', 'device_uid': '87C4F987E5230C58A26E8A8A3E97A8CB', 'phone_model': 'iPad', 'role': '2', 'clientversion': '1.0.0', 'Response': '', 'code': '1', 'msg': '密码错误', 'user_name': ''}, {'account': '13000000000', 'password': '123456', 'system_type': '2', 'system_version': '1.0', 'device_uid': '87C4F987E5230C58A26E8A8A3E97A9CB', 'phone_model': 'iPad', 'role': '3', 'clientversion': '1.0.0', 'Response': '', 'code': '1', 'msg': '用户不存在', 'user_name': ''}]

data1=read_all_req('D:/python/AotoTest/testFile/login/teacherCase.xlsx','login')

@ddt.ddt
class Login(unittest.TestCase):
    def setUp(self):
        self.url='post'
        self.sheet='login'

    def tearDown(self):
        pass

    @ddt.data(*data1)
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
    print(1111)
    print(32222)