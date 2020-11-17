# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 16:39
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_params.py


from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import assert_that, close_to
import pytest


class TestParams:

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
            "unicodeKeyBoard": "true",  # 可以输入中文
            "resetKeyBoard": "true"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass

    @pytest.mark.parametrize("searchkey,type,price", [
        ("阿里巴巴", "BABA", 200),
        ("小米", "01810", 10)
    ])
    def test_search(self, searchkey, type, price):
        '''
        1.打开雪球应用
        2.点击搜索框
        :return:
        '''
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/name").click()
        print("//*[@text=%s]/../../..//*[@resource-id='com.xueqiu.android:id/current_price']" % type)
        text = self.driver.find_element_by_xpath("//*[@text='%s']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']" % type).text
        assert_that(float(text), price)
