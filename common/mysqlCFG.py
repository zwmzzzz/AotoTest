# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 17:57
# @Author  : wenming.zhao
# @Email   : zwm2007@163.com
# @File    : mysqlCFG.py
# @Software: PyCharm
import configparser
import os

from pymysql import connect, OperationalError

base_path=os.path.dirname(__file__)
cfg_path=base_path+'/config.ini'
cf=configparser.ConfigParser()
cf.read(cfg_path,encoding='utf-8')
host = cf.get('MYSQL', 'host')
port = cf.get('MYSQL', 'port')
user = cf.get('MYSQL', 'user')
password = cf.get('MYSQL', 'password')
db_name = cf.get('MYSQL', 'db_name')
charset = cf.get('MYSQL', 'charset')

class DB:
    def __init__(self):
        try:
            self.conn=connect(host=host,port=int(port),user=user,password=password,db=db_name,charset=charset)
        except OperationalError as e:
            print('MySQL error %d: %s' % (e.args[0], e.args[1]))
        else:
            self.cursor = self.conn.cursor()
    def execute_sql(self,command,sql):
        if command in ('select','SELECT'):
            sql=sql.encode('utf-8')
            try:
                self.cursor.execute(sql)
                result=self.cursor.fetchall()
                return result
            except Exception as e:
                print(e)
            finally:
                self.conn.close()

        elif command in ('delete', 'DELETE', 'update', 'UPDATE', 'insert', 'INSERT'):
            sql=sql.encode('utf-8')
            try:
                self.cursor.excute(sql)
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
            finally:
                self.conn.close()