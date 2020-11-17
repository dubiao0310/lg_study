# -*- coding: utf-8 -*-
# @Time    : 2020/11/5 下午5:32
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_window.py
from time import sleep

import pytest
from selenium import webdriver
import os

from selenium.webdriver import ActionChains


class TestWindows:
    def setup(self):
        # browser = os.getenv("browser")
        # if browser == "firefox":
        #     self.driver = webdriver.Firefox()
        # if browser == "chrome":
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_windows(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.current_window_handle) # 查看当前窗口
        print(self.driver.window_handles) # 查看所有窗口
        self.driver.find_element_by_link_text("立即登录").click()

        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1]) # 切换窗口
        # self.driver.find_element_by_id()

    @pytest.mark.skip
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult") # 切换frame
        print(self.driver.find_element_by_id("draggable").text)
        self.driver.switch_to.parent_frame() # 切回父frame
        self.driver.switch_to.default_content()  # 切换默认的frame

    @pytest.mark.skip
    def test_js(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        element = self.driver.execute_script("return document.getElementById('su')") # return 获取返回值
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000") # 滑动到底部
        # 获取title
        # 获取页面性能数据
        # for code in ['return document.title', 'return JSON.stringify(performance.timing)']:
        #     print(self.driver.execute_script(code))
        # 可以合并操作，只返回第一个
        print(self.driver.execute_script('return document.title; return JSON.stringify(performance.timing)'))

    @pytest.mark.skip
    def test_time(self):
        self.driver.get("https://www.12306.cn/index/")
        # removeAttribute 移除时间的readonly属性
        time_element = self.driver.execute_script("a = document.getElementById('train_date');a.removeAttribute('readonly')")
        # 设置时间
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))


    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")  # 切换frame
        # 拖拽
        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        # 切换到弹窗　点击确认
        self.driver.switch_to.alert.accept()
        # 切换到默认frame
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)
