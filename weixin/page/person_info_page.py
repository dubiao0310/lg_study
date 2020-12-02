# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 15:10
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : person_info_page.py
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from weixin.page.base_page import BasePage
from weixin.page.person_operation_page import PersonOperationPage


class PersonInfoPage(BasePage):

    def __init__(self, driver: WebDriver = None, searcher_num=None):
        self._driver = driver
        self.searcher_num = searcher_num

    def goto_person_operation_page(self):
        self.find(MobileBy.ID, "hjz").click()
        return PersonOperationPage(self._driver, self.searcher_num)