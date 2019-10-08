# -*- coding: utf-8 -*-
# @Time    : 2019/5/10 0:10
# @Author  : DannyDong
# @File    : send_email.py
# @describe: 邮件发送相关

import os
import smtplib

from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from Utils.read_ini import ReadIni


class SendEmail(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.info = ReadIni('Sys_config.ini', 'Email')

    def new_report(self):
        report_list = os.listdir(self.file_path)
        report_list.sort(key=lambda fn: os.path.getmtime(self.file_path + "\\" + fn))
        file_new = os.path.join(self.file_path, report_list[-1])
        print("测试结束，报告路径: "+file_new)
        return file_new

    def send_mail(self, report_file):
        # 邮件配置信息
        smtpserver = 'smtp.qq.com'
        user = self.info.get_value('EMAIL_ADDRESS')
        password = self.info.get_value('PASSWORD')
        sender = self.info.get_value('EMAIL_ADDRESS')
        receiver = ["707956456@qq.com"]

        msg = MIMEMultipart()
        msg['Subject'] = Header('UI自动化测试报告', 'utf-8')
        msg["From"] = sender
        msg["To"] = ",".join(receiver)

        # 邮件正文内容
        msg.attach(MIMEText('附件为本次UI自动化测试报告，为保证最佳浏览效果，请使用Chrome打开查看', 'plain', 'utf-8'))

        # 构造附件，传入最新的测试报告文件
        sendfile = open(report_file, 'rb').read()
        att = MIMEText(sendfile, 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="UITestReport.html"'
        msg.attach(att)

        smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
        smtp.connect(smtpserver)
        smtp.login(user, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print("邮件发送成功")

