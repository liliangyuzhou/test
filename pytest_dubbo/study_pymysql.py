#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : study_pymysql.py
# @Author: LILIANG
# @Date  : 2019/5/28
# @Desc  :  test
import pymysql
from Api_liliang2.common.config import config
#1.建立连接：数据库的连接信息：
host=config.get('mysql','host')
user=config.get('mysql','user')
password = config.get('mysql', 'password')
port = int(config.get('mysql', 'port'))
mysql=pymysql.Connect(host=host,user=user,password=password,port=port)
#2新建一个查询页面
cursor=mysql.cursor()
#3.编写SQL
sql='select max(mobilephone) from future.member'
# sql = 'select * from future.loan limit 10'
#4.执行sql
cursor.execute(sql)
# 5.查看结果
result=cursor.fetchone()#获取查询结果集里面最近的一条数据返回
# result=cursor.fetchall()#获取全部的结果集
print(type(result),result)
#6.关闭查询
cursor.close()
# 7关闭数据库连接
mysql.close()
