#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_recharge.py
# @Author: LILIANG
# @Date  : 2019/5/28
# @Desc  :  test

import unittest
from ddt import ddt,data
from Api_liliang1.common.do_excel import *
from Api_liliang1.common.config import config
from Api_liliang1.common import constants
from Api_liliang1.common.http_requests import HttpRequests1

from Api_liliang1.common import logger

logger=logger.my_logger(__name__)


@ddt
class TestRecharge(unittest.TestCase):


    do_excel=DoExcel(constants.case_file,'recharge')
    cases=do_excel.get_cases()

    @classmethod
    def setUpClass(cls):
        logger.info('测试前置')
        cls.http_requests=HttpRequests1()

    @data(*cases)
    def test_recharge(self,case):
        logger.info("{0}测试开始:{1}".format(case.case_id,case.title))
        resp=self.http_requests.requests(case.method,case.url,case.data)
        actual=resp.json()['code']

        try:
            self.assertEqual(str(case.expected),actual)
            self.do_excel.write_result(case.case_id+1,resp.text,'PASS')

        except AssertionError as e:
            self.do_excel.write_result(case.case_id+1,resp.text,'FAIL')
            logger.error("报错了，{0}".format(e))
            raise e

    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置处理')
        cls.http_requests.close()