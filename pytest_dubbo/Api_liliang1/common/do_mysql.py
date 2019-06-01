#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : do_mysql.py
# @Author: LILIANG
# @Date  : 2019/5/28
# @Desc  :  test

import pymysql

class DoMysql:
    """
    完成mysql数据库的交互
    """
    def __init__(self):
        host = 'test.lemonban.com'
        user = 'test'
        password = 'test'
        port = 3306
        # 创建连接
        self.mysql=pymysql.Connect(host=host, user=user, password=password, port=port, charset='utf8')
        #设置查询比并返回字典
        self.cursor=self.mysql.cursor(pymysql.cursors.DictCursor)

    def fetch_one(self,sql):
        self.cursor.execute(sql)
        self.mysql.commit()
         #返回一条数据，元组
        return self.cursor.fetchone()

    def fetch_all(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()#返回一组数据

    def close(self):
        self.cursor.close()
        self.mysql.close()


if __name__ == '__main__':
    mysql=DoMysql()
    sql = 'select max(mobilephone) from future.member'
    result=mysql.fetch_one(sql)
    print(type(result),result)
    sql='select * from future.loan limit 2'
    result=mysql.fetch_all(sql)
    print(type(result), result)

    mysql.close()






