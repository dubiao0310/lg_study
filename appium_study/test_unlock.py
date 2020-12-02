# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 10:52
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_unlock.py

from appium import webdriver


class TestUnlock:

    def setup(self):
        desire_caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            # "appActivity": ".view.WelcomeActivityAlias",
            "appActivity": "com.xueqiu.android.common.MainActivity",
            "noReset": True,  # 解决更新弹窗、登陆等,
            # "dontStopAppOnReset": "true",  # 首次启动时，不重停止app
            "skipDeviceInitialization": "true",  # 跳过安装，设置权限等操作
            "unicodeKeyBoard": "true"  # 可以输入中文
        }
        self.driver = webdriver.Remote()


    def teardown(self):
        pass
