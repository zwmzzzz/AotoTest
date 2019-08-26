# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 15:19
# @Author  : wenming.zhao
# @Email   : zwm2007@163.com
# @File    : readExcel.py
# @Software: PyCharm
import xlrd as xlrd


def cell_value(fp,sheet_name,row,col):
    test_data=xlrd.open_workbook(fp)
    sheet_name=test_data.sheet_by_name(sheet_name)
    return sheet_name.cell_value(row-1,col-1)

def row_value(fp,sheet_name,case_name):
    test_data=xlrd.open_workbook(fp,'br')
    sheet_name=test_data.sheet_by_name(sheet_name)
    cases=sheet_name.col_values(0)
    for case_i in range(len(cases)):
        if cases[case_i] == case_name :
            return sheet_name.row_values(case_i)

def col_value(fp,sheet_name,col):
    test_data=xlrd.open_workbook(fp)
    sheet_name=test_data.sheet_by_name(sheet_name)
    return sheet_name.col_values(col-1)


def read_all_req(fp,sheet_name):
    print("fp:",fp)
    test_data=xlrd.open_workbook(fp)
    sheet_name=test_data.sheet_by_name(sheet_name)
    row=sheet_name.nrows
    print(row)
    col=sheet_name.ncols
    print(col)

    param_key =sheet_name.row_values(0)
    for i in range(len(param_key)):
        if param_key[i] == 'Response':
            req_len = i
            break

    data_list=[]
    for i in range(1,row):
        dict={}
        for j in range(1,col):
            dict[sheet_name.cell_value(0,j)]=sheet_name.cell_value(i,j)
        data_list.append(dict)
    return data_list

if __name__=='__main__':
    read_all_req()
