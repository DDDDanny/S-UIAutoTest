# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 13:26
# @Author  : DannyDong
# @File    : driver.py
# @describe: 浏览器Driver

from selenium import webdriver


class SelectBrowser(object):
    def __init__(self):
        self.browser_dict = {
            'chrome': webdriver.Chrome,
            'firefox': webdriver.Firefox,
            'edge': webdriver.Edge,
            'ie': webdriver.Ie
        }

    def select_browser(self, browser='chrome'):
        try:
            if browser == 'chrome':
                dr = self.browser_dict[browser]
            elif browser == 'firefox':
                dr = self.browser_dict[browser]
            elif browser == 'edge':
                dr = self.browser_dict[browser]
            elif browser == 'ie':
                dr = self.browser_dict[browser]
            else:
                raise Exception('没有找到名字为"{0}"的浏览器'.format(browser))
            return dr()
        except Exception:
            raise NameError('没有找到名字为"{0}"的浏览器'.format(browser))


if __name__ == '__main__':
    demo = SelectBrowser()
    demo.select_browser('chrome')
