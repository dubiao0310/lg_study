# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 下午3:18
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : login.py
from selenium.webdriver.common.by import By

from page_object.page.base_page import BasePage
from page_object.page.register import Register


class Login(BasePage):

    def scan(self):
        pass

    def goto_login(self):
        self.find(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return Register(self._driver)
