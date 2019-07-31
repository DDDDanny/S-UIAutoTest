# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 14:27
# @Author  : DannyDong
# @File    : demo_page.py
# @describe: 页面层

from PySe.operation import PySelenium


class DemoPage(object):
    def __init__(self, driver):
        self.element = PySelenium(driver)

    # 输入关键字
    def send_keywords(self, keywords):
        self.element.input_element('SearchInfo', 'search_input', keywords)

    # 点击提交信息
    def click_submit(self):
        self.element.click_element('SearchInfo', 'submit')

    # 获取wording信息
    def get_wording(self):
        return self.element.get_element_text('SearchInfo', 'nums_text')

    # 获取当前页面url
    def get_url(self):
        return self.element.get_current_url()
