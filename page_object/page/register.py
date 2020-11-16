# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 下午3:10
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : register.py
from selenium.webdriver.common.by import By

from page_object.page.base_page import BasePage


class Register(BasePage):

    def register(self):
        self.find(By.ID, "corp_name").send_keys("hello")
        self.find(By.ID, "manager_name").send_keys("hello2")
        return True