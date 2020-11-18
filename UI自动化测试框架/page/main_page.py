# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 16:04
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : main_page.py
from selenium.webdriver.common.by import By

from UI自动化测试框架.page.base_page import BasePage


class Main(BasePage):

    # def goto_search(self):
    #     # return self.find(By.ID, "tv_search").click()
    #     self.steps("..\page\main.yaml")

    def goto_edit(self):
        self.find(By.ID, "post_status").click()
        self.find(By.ID, "tv_search").click()

