# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 17:28
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : main_page.py
from appium.webdriver.common.mobileby import MobileBy

from weixin.page.base_page import BasePage
from weixin.page.contact_list_page import ContactList


class MainPage(BasePage):

    def goto_contact(self):
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return ContactList(self._driver)