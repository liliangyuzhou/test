#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : study_reflect.py
# @Author: LILIANG
# @Date  : 2019/5/31
# @Desc  :  test

class people:
    common_eyes=2
    def __init__(self,name,age):
        self.name=name
        self.age=age


if __name__ == '__main__':
    p=people('name','age')
    print(p.name)
    print(p.age)
    print(people.common_eyes)
    print(hasattr(p,'name'))
    setattr(people,"legs",2)
    # print(people.legs)
    print(getattr(people,'legs'))
    delattr(people,'legs')

    print(getattr(people, 'legs'))

