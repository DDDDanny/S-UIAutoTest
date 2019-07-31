# -*- coding: utf-8 -*-
# @Time    : 2019/5/10 0:10
# @Author  : DannyDong
# @File    : send_email.py
# @describe: 邮件发送相关

import smtplib
import os

from email.mime.text import MIMEText
from email.header import Header

from config.sys_config import *


def send_mail(report):
    f = open(report, 'rb')
    mail_content = f.read()
    f.close()

    smtp_server = SMTP
    user = EMAIL_ADDRESS
    password = PASSWORD
    sender = EMAIL_ADDRESS
    receives = RE_EMAIL_ADDRESS
    subject = 'UI自动化测试报告'

    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg["From"] = sender
    msg["To"] = ','.join(receives)

    smtp = smtplib.SMTP_SSL(smtp_server, 465)
    smtp.helo(smtp_server)
    smtp.ehlo(smtp_server)
    smtp.login(user, password)
    print('正在发送邮件>>>>>>>')
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    print("邮件已发出，请注意查收!")


# 查找最新的报告
def latest_report(report_dir):
    # 将目录下文件存入list中
    lists = os.listdir(report_dir)
    # 排序
    lists.sort(key=lambda fn: os.path.getmtime(report_dir + "\\" + fn))
    # 取出最后一个文件，即最新的报告
    file = os.path.join(report_dir, lists[-1])
    # print(file)
    return file

