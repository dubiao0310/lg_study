# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 15:15
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : person_operation_page.py
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from weixin.page.base_page import BasePage
from weixin.page.edit_contact_page import EditContactPage


class PersonOperationPage(BasePage):

    def __init__(self, driver: WebDriver = None, searcher_num=None):
        self._driver = driver
        self.searcher_num = searcher_num


    def goto_edit_contact_page(self):
        self.find(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        return EditContactPage(self._driver, self.searcher_num)