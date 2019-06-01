#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : study_json.py
# @Author: LILIANG
# @Date  : 2019/5/25
# @Desc  :  数据类型的转换 str-->dict

"""
json是一种数据格式
json的特点
json中的字符串必须用双引号引起来，
json中不含有有None，只含有null
json中的的list以及array数据以[]表示
json中的true和false只有小写，而python中的true和false都是首字母大写

python中的字典
Python中的字符串（键值对，看起来本身就像字典的数据，可能只是在字典外加了''或者"")
是可以转换为字典格式的（转换为字典是因为post和get传参，都是字典形式），
可以通过eval函数，但是eval函数只能将字符串转换成python中已有的数据类型，当字符串中含有
null时，该含有null的字符串是不能使用eval函数直接转换为字典格式的数据.这时候就只能使用
json模块中的loads方法将字符串转为字典


json：
json中的load和loads方法：将字符串转换为字典
json中的dump和dumps方法：将字典反转为字符串

所以，一般什么时候使用eval转换字符串为词典，什么时候使用json？
一般数据的入参，我们使用eval函数将字符串转换为词典
一般的返回值（出参），因为是从java程序的返回值，所以可能含有python中没有的字符，比如null
所以这里使用json中的loads方法将字符串转换为词典
params = '{"status":1,"code":"10001","data":null,"msg":"登录成功"}'
d=eval(params)
print(d)

为什么要在出参时候转换为字典格式，一般都是字符串格式？
因为有的时候我们将实际的返回值与期望值作对比，相当于断言，但是类似于查询接口，每次的返回值可能
都不尽相同，全部匹配相等很困难，而我们只取 返回值  其中的一部分，进行断言，转换为字典，方便根据key
来取到我们需要的值来进行断言。
"""
# 正常的json格式
# {"key":[]}

params = '{"status":1,"code":"10001","data":null,"msg":"登录成功"}'
# d=eval(params)
# print(d)
import json
d1=json.loads(params)
print(type(d1),d1)
print(d1['msg'])

