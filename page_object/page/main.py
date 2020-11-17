# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 下午2:49
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : main.py
from selenium.webdriver.common.by import By

from page_object.page.base_page import BasePage
from page_object.page.login import Login
from page_object.page.register import Register


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/"

    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self._driver)

    def goto_login(self):
        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return Login(self._driver)
