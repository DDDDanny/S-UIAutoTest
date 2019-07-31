# -*- coding: utf-8 -*-
# @Time    : 2019/6/9 18:25
# @Author  : DannyDong
# @File    : read_ini.py.py
# @describe: 读取配置文件

import configparser


class ReadIni(object):
    # 构造函数
    def __init__(self, file_name=None, node=None):
        if file_name is None:
            file_name = './Config/Ele_config.ini'

        if node is None:
            self.node = 'LoginPage'
        else:
            self.node = node

        self.conf = self.load_ini(file_name)

    # 加载文件
    @staticmethod
    def load_ini(file_name):
        conf = configparser.ConfigParser()
        conf.read(file_name)
        return conf

    # 获取Value值
    def get_value(self, key):
        data = self.conf.get(self.node, key)
        return data


if __name__ == '__main__':
    # read = ReadIni()
    read = ReadIni('../Config/Sys_config.ini', 'Report')
    print(read.get_value('REPORTURL'))
