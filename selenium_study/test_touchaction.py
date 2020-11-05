# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 下午6:07
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_touchaction.py
from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchaction:

    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_touch(self):
        self.driver.get("https://www.baidu.com/")
        el = self.driver.find_element_by_id("kw")
        el_search = self.driver.find_element_by_id("su")

        el.send_keys("selenium测试")
        action = TouchActions(self.driver)
        # 点击搜索
        action.tap(el_search)
        action.perform()
        # 滑动到最下边
        action.scroll_from_element(el, 0, 1000).perform()