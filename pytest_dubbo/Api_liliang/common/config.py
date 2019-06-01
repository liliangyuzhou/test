#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : config.py
# @Author: LILIANG
# @Date  : 2019/5/27
# @Desc  :  test


import configparser
from Api_liliang.common import constants

class ReadConfig:
    def __init__(self):
        self.config=configparser.ConfigParser()
        self.config.read(constants.global_file)
        switch=self.config.getboolean('switch','on')
        if switch:#开关状态为打开状态
            self.config.read(constants.online_file,encoding='utf-8')
        else:
            self.config.read(constants.test_file,encoding='utf-8')
    def get(self,section,option):
        return self.config.get(section,option)


config=ReadConfig()