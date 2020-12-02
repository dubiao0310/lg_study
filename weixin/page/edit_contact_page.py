# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 15:19
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : edit_contact_page.py
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from weixin.page.base_page import BasePage



class EditContactPage(BasePage):

    def __init__(self, driver: WebDriver = None, searcher_num=None):
        self._driver = driver
        self.searcher_num = searcher_num

    def goto_searcher_contact_page(self):
        self.find(MobileBy.XPATH, "//*[@text='删除成员']").click()
        self.find(MobileBy.XPATH, "//*[@text='确定']").click()
        from weixin.page.searcher_contact_page import SearcherContactPage
        return SearcherContactPage(self._driver, self.searcher_num)