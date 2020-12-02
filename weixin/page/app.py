# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 17:19
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : app.py
from appium import webdriver

from weixin.page.base_page import BasePage
from weixin.page.main_page import MainPage


class App(BasePage):

    def start(self):
        caps = {
            "platformName": "Android",
            "deviceName": "P7C0218119005759",
            "appPackage": "com.tencent.wework",
            "appActivity": "com.tencent.wework.launch.WwMainActivity",
            "noReset": "True",
            "skipDeviceInitialization": "true",  # 跳过安装，设置权限等操作
            "unicodeKeyBoard": "true",  # 可以输入中文
            "resetKeyBoard": "true"
        }

        if self._driver == None:
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        else:
            self._driver.launch_app()

        self._driver.implicitly_wait(5)
        return self

    def restart(self):
        pass

    def stop(self):
        self._driver.quit()

    def goto_main(self):
        return MainPage(self._driver)
