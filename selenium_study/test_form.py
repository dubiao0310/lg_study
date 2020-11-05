# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 下午8:45
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_form.py
import time

from selenium import webdriver


class TestForm:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("1111")
        self.driver.find_element_by_id("user_password").send_keys("1234")
        self.driver.find_element_by_id("user_remember_me").click()
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input').click()
        time.sleep(3)