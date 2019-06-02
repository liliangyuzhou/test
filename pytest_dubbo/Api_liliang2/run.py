#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : run.py
# @Author: LILIANG
# @Date  : 2019/5/29
# @Desc  :  test

import unittest
from Api_liliang2.common import HTMLTestRunnerNew
from Api_liliang2.common import constants



discover=unittest.defaultTestLoader.discover(constants.cases_file,"test_*.py")
with open(constants.report_file + '/report.html','wb+') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                         verbosity=2,
                                         title="测试报告",
                                         description="tester",
                                         tester="李亮")
    runner.run(discover)


