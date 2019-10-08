# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 14:29
# @Author  : DannyDong
# @File    : demo_case.py
# @describe: demo用例

import time
import unittest

from Test.Case.base_case import BaseCase
from Utils.get_log import LogInfo


class DemoCase(BaseCase, LogInfo):
    """ Demo测试用例 """

    # @unittest.skip('case skip')
    @LogInfo.get_error
    def test_keywords_null(self):
        """ 关键字为空 """
        url = self.demo.keywords_null('')
        self.log.info('测试日志')
        self.assertEqual('https://www.baidu.com/', url, '关键字为空 --- 测试不通过')

    # @unittest.skip('case skip')
    @LogInfo.get_error
    def test_search_keywords(self):
        """ 正常搜索 """
        info = self.demo.search_keywords('python')
        self.assertEqual('百度为您找到相关结果约100,000,000个', info, '正常搜索 --- 测试不通过')


if __name__ == '__main__':
    unittest.main()
    time.sleep(5)
