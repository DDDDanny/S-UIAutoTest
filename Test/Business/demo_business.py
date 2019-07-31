# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 14:28
# @Author  : DannyDong
# @File    : demo_business.py
# @describe: 业务层

from Test.Page.demo_page import DemoPage


class DemoBusiness(object):
    def __init__(self, driver):
        self.demo_Business = DemoPage(driver)

    # 关键字为空
    def keywords_null(self, keywords):
        self.demo_Business.send_keywords(keywords)
        return self.demo_Business.get_url()

    # 正常输入关键字
    def search_keywords(self, keywords):
        self.demo_Business.send_keywords(keywords)
        return self.demo_Business.get_wording()
