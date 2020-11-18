# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 15:33
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : app.py
import yaml
from appium import webdriver

from UI自动化测试框架.page.base_page import BasePage
from UI自动化测试框架.page.main_page import Main


class App(BasePage):

    def start(self):
        if self._dirver == None:
            desire_caps = {
                "platformName": "Android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.xueqiu.android",
                "appActivity": ".view.WelcomeActivityAlias",
                "noReset": True,  # 解决更新弹窗、登陆等,
                # "dontStopAppOnReset": "true",  # 首次启动时，不重停止app
                "skipDeviceInitialization": "true",  # 跳过安装，设置权限等操作
                "unicodeKeyBoard": "true",  # 可以输入中文
                "resetKeyBoard": "true",
                "udid": yaml.safe_load(open("../page/config.yaml"))["caps"]["udid"]
            }
            self._dirver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        else:
            # self._dirver.launch_app()
            self._dirver.start_activity("com.xueqiu.android", ".view.WelcomeActivityAlias") # 等同launch_app
        self._dirver.implicitly_wait(5)
        return self

    def main(self) -> Main:
        return Main(self._dirver)