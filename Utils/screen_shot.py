# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 18:45
# @Author  : DannyDong
# @File    : screen_shot.py
# @describe: 截图方法

import sys
import time

from selenium import webdriver

from Utils.read_ini import ReadIni


class ScreenShot(object):
    def __init__(self):
        read_ini = ReadIni('./Config/Sys_config.ini', 'HotScreen')
        self.url = read_ini.get_value('SCREENSHOTURL')

    def screen_shot(self, driver):
        if driver is not None:
            new_url = sys._getframe(0).f_code.co_name + time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            driver.get_screenshot_as_file(self.url + new_url + '.png')
        else:
            raise Exception('Error! 参数错误！')


if __name__ == '__main__':
    driver1 = webdriver.Chrome()
    demo = ScreenShot()
    demo.screen_shot(driver1)
    driver1.close()
