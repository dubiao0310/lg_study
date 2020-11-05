# -*- coding: utf-8 -*-
# @Time    : 2020/11/3 下午5:12
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_click.py
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.common.keys import Keys


class TestClick:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_lick(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element(By.XPATH, '//*[@name="f1"]//input[3]')
        element_doubleclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        sleep(2)
        action.perform()
        sleep(2)

    @pytest.mark.skip
    def test_moveto(self):
        self.driver.get("http://www.baidu.com")
        ele = self.driver.find_element_by_link_text("设置")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element_by_id("dragger")
        drop_element = self.driver.find_element_by_xpath("/html/body/div[2]")
        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_element, drop_element).perform()
        action.click_and_hold(drag_element).release(drop_element).perform() # 等同上面方法

    # @pytest.mark.skip
    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)   # pause(1) 等待１秒
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom")
        action.send_keys(Keys.BACK_SPACE).perform()


