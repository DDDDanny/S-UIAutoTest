# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 13:28
# @Author  : DannyDong
# @File    : operation.py
# @describe: 二次封装selenium

import time

from Utils.read_ini import ReadIni
from Utils.screen_shot import ScreenShot

from selenium.webdriver.common.keys import Keys


class PySelenium(object):

    # 构造函数
    def __init__(self, driver):
        self.driver = driver
        self.wait_wait()
        self.wait_time = 0.5

    # 获取元素
    def get_element(self, node_kw, key):
        read_ini = ReadIni(node=node_kw)
        data = read_ini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        num = int(data.split('>')[2])

        try:
            if by == 'id':
                return self.driver.find_elements_by_id(value)[num]
            elif by == 'name':
                return self.driver.find_elements_by_name(value)[num]
            elif by == 'classname':
                return self.driver.find_elements_by_class_name(value)[num]
            elif by == 'xpath':
                return self.driver.find_elements_by_xpath(value)[num]
        except Exception:
            ScreenShot().screen_shot(self.driver)
            raise NameError('选择器错误！')

    # 浏览器最大化
    def maximize_window(self):
        self.driver.maximize_window()

    # 刷新页面
    def f5(self):
        self.driver.refresh()

    # get地址
    def test_url(self, url):
        self.driver.get(url)

    # 获取当前页面URL
    def get_current_url(self):
        return self.driver.current_url

    # 全局隐式等待
    def wait_wait(self):
        self.driver.implicitly_wait(3)

    # 强制等待
    def sleep(self):
        time.sleep(self.wait_time)

    # 右键点击元素
    def click_element(self, node_kw, key):
        try:
            element = self.get_element(node_kw, key)
            self.sleep()
            element.click()
        except Exception:
            ScreenShot().screen_shot(self.driver)
            raise ValueError('element错误！')

    # 通过使用JS进行点击操作
    def js_click_element(self, node_kw, key):
        try:
            element = self.get_element(node_kw, key)
            self.sleep()
            self.driver.execute_script("arguments[0].click();", element)
            self.sleep()
        except Exception:
            ScreenShot().screen_shot(self.driver)
            raise ValueError('element错误！')

    # 输入内容
    def input_element(self, node_kw, key, content):
        try:
            element = self.get_element(node_kw, key)
            self.sleep()
            element.send_keys(content)
        except Exception:
            ScreenShot().screen_shot(self.driver)
            raise ValueError('element错误！')

    # 获取元素text
    def get_element_text(self, node_kw, key):
        try:
            self.sleep()
            return self.get_element(node_kw, key).text
        except Exception:
            ScreenShot().screen_shot(self.driver)
            raise ValueError('element错误！')

    # 清空元素内容
    def element_clear(self, node_kw, key):
        try:
            element = self.get_element(node_kw, key)
            self.sleep()
            element.clear()
        except Exception:
            ScreenShot().screen_shot(self.driver)
            raise ValueError('element错误！')

    # 强制清除内容，模拟键盘操作，先ctrl+a再Delete
    def element_force_clear(self, node_kw, key):
        try:
            element = self.get_element(node_kw, key)
            self.sleep()
            element.send_keys(Keys.CONTROL, 'a')
            element.send_keys(Keys.DELETE)
        except Exception:
            ScreenShot().screen_shot(self.driver)
            raise ValueError('element错误！')


if __name__ == '__main__':
    # demo = PySelenium()
    pass
