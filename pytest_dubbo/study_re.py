#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : study_re.py
# @Author: LILIANG
# @Date  : 2019/5/30
# @Desc  :  test
import re
from Api_liliang2.common.config import config
# data = '{"mobilephone":"normal_user","pwd":"normal_pwd"}'
# p='normal_user'
# n=re.search(p,data)
# print(n)
data = '{"mobilephone":"#normal_user#","pwd":"#normal_pwd#"}'
# data1 = '{"mobilephone":"#normal_user#","pwd":"#normal_pwd#"}'
# 原本字符,元字符
p = "#(.*?)#"  # 正则表达式
# ms = re.findall(p, data1)  # 查找全部，返回列表
# print(type(ms),ms)
#
# m=re.search(p,data1)
# # print(type(m),m)
# # print(m.group(1))
# x=m.group(1)
# v=config.get('data',x)
# print(v)
# data_new=re.sub(p,v,data1,count=1)
# print(data_new)

# 如果要匹配多次，替换多次，使用循环来解决

while re.search(p, data):
    print(data)
    m = re.search(p, data)  # 从任意位置开始找，找第一个就返回Match object, 如果没有找None
    g = m.group(1)  # 拿到参数化的KEY
    v = config.get('data', g)  # 根据KEY取配置文件里面的值
    print(v)
    # 记得替换后的内容，继续用data接收
    data = re.sub(p, v, data, count=1)  # 查找替换,count查找替换的次数

print('最后替换后的data', data)