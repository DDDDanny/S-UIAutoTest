# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 12:50
# @Author  : DannyDong
# @File    : demo_suite.py
# @describe: 测试用例集合

import unittest

from ..Case.demo_case import DemoCase


def case_suite():
    suite = unittest.TestSuite()
    # 新增用例集
    suite.addTest(DemoCase('test_keywords_null'))
    suite.addTest(DemoCase('test_search_keywords'))

    return suite
