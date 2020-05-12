# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 13:28
# @Author  : DannyDong
# @File    : operation.py
# @describe: 二次封装selenium

import time
import random

from Utils.read_ini import ReadIni

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec


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
        element = None

        try:
            web_driver_wait = WebDriverWait(self.driver, 10, 0.5)
            if by == 'id':
                element = web_driver_wait.until(ec.presence_of_all_elements_located((By.ID, value)))
            elif by == 'name':
                element = web_driver_wait.until(ec.presence_of_all_elements_located((By.NAME, value)))
            elif by == 'classname':
                element = web_driver_wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME, value)))
            elif by == 'xpath':
                element = web_driver_wait.until(ec.presence_of_all_elements_located((By.XPATH, value)))
            elif by == 'tag':
                element = web_driver_wait.until(ec.presence_of_all_elements_located((By.TAG_NAME, value)))
            elif by == 'css':
                element = web_driver_wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, value)))
        # 页面未找到该元素，返回False
        except (NoSuchElementException, IndexError, TimeoutException):
            return False
        # 没有发生异常，说明已找到该元素，返回该元素
        else:
            return element[num]

    # 浏览器最大化
    def maximize_window(self):
        self.driver.maximize_window()

    # 页面滑动到底部(页面滑动到顶部:h=0)
    def page_sliding_to_footer(self, node_kw, key, h=100000):
        read_ini = ReadIni(node=node_kw)
        data = read_ini.get_value(key)
        value = data.split('>')[1]
        num = int(data.split('>')[2])
        js = "var q=document.getElementsByClassName('{}')[{}].scrollTop={}".format(value, num, h)
        self.driver.execute_script(js)

    # 页面滑动到最右边(页面滑动到最左:long=0)
    def page_sliding_to_right(self, node_kw, key, long=100000):
        read_ini = ReadIni(node=node_kw)
        data = read_ini.get_value(key)
        value = data.split('>')[1]
        num = int(data.split('>')[2])
        js = "var q=document.getElementsByClassName('{}')[{}].scrollLeft={}".format(value, num, long)
        self.driver.execute_script(js)

    # 刷新页面
    def f5(self):
        self.driver.refresh()

    # get地址
    def test_url(self, url):
        self.driver.get(url)

    # 获取当前页面URL
    def get_current_url(self):
        self.sleep()
        return self.driver.current_url

    # 全局隐式等待
    def wait_wait(self):
        self.driver.implicitly_wait(10)

    # 强制等待
    def sleep(self):
        time.sleep(self.wait_time)

    # 切换新页面
    def switch_windows(self, index):
        time.sleep(1)
        # index: 页面的索引
        self.driver.switch_to.window(self.driver.window_handles[index])
        time.sleep(1)

    # 判断元素是否可见
    def element_is_display(self, node_kw, key):
        try:
            element = self.get_element(node_kw, key)
            return element.is_displayed()
        except Exception:
            raise ValueError('元素未找到！or 元素操作错误！')

    # 右键点击元素
    def click_element(self, node_kw, key):
        try:
            element = self.get_element(node_kw, key)
            element.click()
            self.sleep()
        except Exception:
            raise ValueError('元素未找到！or 元素操作错误！')

    # 鼠标悬停事件
    def move_to_element(self, node_kw, key):
        element = self.get_element(node_kw, key)
        ActionChains(self.driver).move_to_element(element).perform()

    # 通过使用JS进行点击操作
    def js_click_element(self, node_kw, key):
        try:
            element = self.get_element(node_kw, key)
            self.driver.execute_script("arguments[0].click();", element)
            self.sleep()
        except Exception:
            raise ValueError('元素未找到！or 元素操作错误！')

    # 输入内容
    def input_element(self, node_kw, key, content):
        try:
            element = self.get_element(node_kw, key)
            element.send_keys(content)
        except Exception:
            raise ValueError('元素未找到！or 元素操作错误！')

    # 获取元素text
    def get_element_text(self, node_kw, key):
        try:
            self.sleep()
            element = self.get_element(node_kw, key)
            return element.text
        except Exception:
            raise ValueError('元素未找到！or 元素操作错误！')

    # 获取输入框中的值
    def get_input_value(self, node_kw, key):
        try:
            element = self.get_element(node_kw, key)
            return element.get_attribute('value')
        except Exception:
            raise ValueError('元素未找到！or 元素操作错误！')

    # 获取下拉菜单选项
    def get_ul_li(self, node_kw, key, li_num=None):
        try:
            self.sleep()
            element = self.get_element(node_kw, key)
            element_li = element.find_elements_by_css_selector('li')
            if li_num is None:
                count = len(element_li)
                i = random.randint(0, count - 1)
                self.driver.execute_script("arguments[0].click();", element_li[i])
            else:
                self.driver.execute_script("arguments[0].click();", element_li[li_num])
        except Exception:
            raise ValueError('元素未找到！or 元素操作错误！')

    # 获取表格表头
    def get_tr_th(self, node_kw, key, td_num):
        try:
            element = self.get_element(node_kw, key)
            return element.find_elements_by_css_selector('tr')[0].find_elements_by_css_selector('th')[td_num].text
        except Exception:
            raise ValueError('元素未找到！or 元素操作错误！')

    # 获取表格数据
    def get_tr_td_desc(self, node_kw, key, td_num):
        try:
            self.sleep()
            element = self.get_element(node_kw, key)
            return element.find_elements_by_css_selector('tr')[0].find_elements_by_css_selector('td')[td_num].text
        except Exception:
            raise ValueError('元素未找到！or 元素操作错误！')

    # 清空元素内容
    def element_clear(self, node_kw, key):
        try:
            element = self.get_element(node_kw, key)
            element.clear()
        except Exception:
            raise ValueError('元素未找到！or 元素操作错误！')

    # 强制清除内容，模拟键盘操作，先ctrl+a再Delete
    def element_force_clear(self, node_kw, key):
        try:
            element = self.get_element(node_kw, key)
            element.send_keys(Keys.CONTROL, 'a')
            element.send_keys(Keys.DELETE)
        except Exception:
            raise ValueError('元素未找到！or 元素操作错误！')

    # 向富文本编辑器中填写内容
    def input_text_editor(self, node_kw, key, content):
        try:
            element = self.get_element(node_kw, key)
            self.driver.switch_to.frame(element)
            self.driver.find_elements_by_tag_name('body')[0].send_keys(content)
            self.sleep()
            # 切回主窗口
            self.switch_windows(0)
            self.sleep()
        except Exception:
            raise ValueError('元素未找到！or 元素操作错误！')


if __name__ == '__main__':
    # demo = PySelenium()
    pass
