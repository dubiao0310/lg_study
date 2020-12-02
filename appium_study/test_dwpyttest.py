# -*- coding: utf-8 -*-
# @Time    : 2020/11/12 21:05
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_dwpyttest.py
from appium import webdriver
import pytest
from appium.webdriver.common.touch_action import TouchAction


class TestDw:

    def setup(self):
        # com.xueqiu.android/.view.WelcomeActivityAlias
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

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(10)


    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_dw(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]').click()

    @pytest.mark.skip
    def test_attr(self):
        elemrnt = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(elemrnt.text)
        print(elemrnt.location) # 获取坐标
        print(elemrnt.size) # 获取宽和高
        if elemrnt.is_enabled():  # 判断是否可用
            elemrnt.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
            albb_element = self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]')
            # albb_element.is_displayed() # 是否可见
            element_display = albb_element.get_attribute("displayed")
            if element_display == "true":
                print("搜索成功")


    def test_touchaction(self):
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect() # 获取当前页面的尺寸
        width = window_rect["width"]
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height * 4/5)
        y_stop = int (height * 1/5)
        # action.press(x=731, y=2083).wait(200).move_to(x=731, y=484).release().perform()
        action.press(x=x1, y=y_start).wait(2000).move_to(x=x1, y=y_stop).release().perform()


