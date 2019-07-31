# S-UIAutoTest
This is a simple UI Auto Test👻

### 概述

​	S-UIAutoTest是基于Python+Selenium+Unittest的UI自动化测试框架，采用了PO（Page Object）设计模式，将页面对象与用例进行分离，提高了代码的复用性，降低了维护成本。

### 功能

- [x] 生成测试报告
- [x] 自动截图
- [x] 自动发送测试报告
- [ ] 生成运行日志

###  系统结构

|          分层结构           |
| :-------------------------: |
| 用例集合（TestCases Suite） |
|     用例层（TestCase）      |
|     业务层（Business）      |
|       页面层（Page）        |
| Python对Selenium的二次封装  |



### 目录结构

├─ Config  配置文件目录<br>│  │  Ele_config.ini  元素配置文件<br>│  │  Sys_config.ini  系统配置文件<br>│<br>├─Media  媒体文件（图片、音频、视频等）<br>│<br>├─PySe<br>│  │  driver.py  浏览器驱动选择器<br>
│  │  operation.py  对Selenium的二次封装<br>│<br>├─Test<br>│  ├─Page  页面层<br>│  │  │  demo_page.py<br>
│  ├─Business  业务层<br>│  │  │  demo_business.py<br>
│  ├─Case  用例层<br>│  │  │  base_case.py  Case基类<br>│  │  │ demo_case.py<br>
│  ├─CaseSuite  用例集合<br>│  │  │  case_suite.py<br>│<br>├─Utils  工具库<br>│  │ HTMLTestRunner.py  HTMLTestRunner测试报告<br>│  │ HTMLTestRunner_cn.py  HTMLTestRunner测试报告<br>│  │ read_ini.py  读取配置文件<br>│  │ screen_shot.py  截图工具<br>│  │ send_email.py  发送邮件<br>│<br>├─Result  测试结果<br>│  ├─HotScreen  截图目录<br>│  ├─Report  测试报告<br>│<br>└─run.py  程序入口<br>

### 说明

##### 1. 元素配置及读取

Ele_config.ini

```ini
[SearchInfo]
search_input = id>kw>0
submit = classname>s_btn>0
nums_text = classname>nums_text>0
```
operation.py

```python
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
```

+ 读取元素使用的区分符号是“>”，这个可以根据需求进行修改
+ 支持的选择器有：id、name、classname、xpath，可以根据需求进行添加

##### 2. 浏览器选择器

```python
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
```

+ 支持chrome、firefox、edge、ie，可以根据需求进行添加

### 感谢

感谢Rong Che大佬的帮助：<https://github.com/CrDym>

感谢虫师的pyse项目：<https://github.com/defnngj/pyse>

感谢HTMLTestRunner的作者：<https://github.com/findyou/HTMLTestRunnerCN>

