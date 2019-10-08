# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 13:23
# @Author  : DannyDong
# @File    : run.py
# @describe: 程序主入口

import time

from Utils.read_ini import ReadIni
from Utils.send_email import SendEmail
from Utils.HTMLTestRunner_cn import HTMLTestRunner
from Test.CaseSuite.case_suite import case_suite

suite = case_suite()

read_ini = ReadIni('Sys_config.ini', 'Report')
url = read_ini.get_value('REPORTURL')

if __name__ == '__main__':
    filename = url + time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + 'result.html'
    fp = open(filename, 'wb')

    runner = HTMLTestRunner(
        stream=fp,
        title='UI自动化测试报告',
        description='Demo Test'
    )
    runner.run(suite)
    fp.close()

    # 发送邮件开关is_debug,debug模式下，不发送邮件
    if ReadIni('Sys_config.ini', 'Base').get_value('is_debug') == 'True':
        # 实例化对象
        demo = SendEmail(url)
        # 获取最新报告
        new_report = demo.new_report()
        # 发送测试报告
        demo.send_mail(new_report)
    else:
        pass
