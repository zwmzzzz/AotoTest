# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 15:31
# @Author  : wenming.zhao
# @Email   : zwm2007@163.com
# @File    : getParams.py
# @Software: PyCharm
import configparser
import os

from common.readExcel import row_value, read_all_req

proj_path=str(os.path.dirname(__file__).split('common')[0])
proj_path=proj_path.replace('\\','/')
excel_path=proj_path+'testFile/login/teacherCase.xlsx'
cfg_path=proj_path+'/config.ini'
cf=configparser.ConfigParser()
cf.read(cfg_path,encoding='utf-8')

def get_req_params(sheet,case):
    req_len=0
    param_key=row_value(excel_path,sheet,'case_name')
    param_value=row_value(excel_path,sheet,case)
    for i in range(len(param_key)):
        if param_key[i]=='Response':
            req_len=i
            break
    params=dict()
    for key_i in range(1,req_len):
        params[param_key[key_i]]=param_value[key_i]

    return params

def get_resp_params(sheet, case, resp_key):
        resp_len=0
        param_key=row_value(excel_path,sheet,'case_name')
        param_value=row_value(excel_path,sheet,case)
        for i in range(len(param_key)):
            if param_key[i]=='Response':
                resp_len=i+1
                break

        for key_i in range(resp_len,len(param_key)):
            if param_key[key_i]==resp_key:
                return param_value[key_i]



if __name__=='__main__':
    #req=get_req_params('login','test_login_success')
   # print(req)
    #req1=get_resp_params('login','test_login_success','msg')
    #print(req1)
    print(excel_path)
    req2=read_all_req(excel_path,'login')




