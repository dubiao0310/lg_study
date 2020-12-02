# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 18:31
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : searcher_contact_page.py
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from weixin.page.base_page import BasePage
from weixin.page.person_info_page import PersonInfoPage


class SearcherContactPage(BasePage):

    def __init__(self, driver: WebDriver = None, searcher_num=None):
        self._driver = driver
        self.searcher_num = searcher_num

    def goto_person_info_page(self, name=None):
        self.find(MobileBy.ID, "g75").send_keys(name)
        WebDriverWait(self._driver, 5).until(expected_conditions.visibility_of_element_located,
                                            (MobileBy.XPATH, "//*[@text='联系人']"))
        sleep(3)
        elements = self.finds(MobileBy.ID, "ddw")
        # if self.searcher_num is None:
        if len(elements) >= 1:
            elements[0].click()
            return PersonInfoPage(self._driver, len(elements))
        # else:
        #     print(elements)
        #     return self.searcher_num, len(elements)

    def get_elements(self):
        WebDriverWait(self._driver, 5).until(expected_conditions.visibility_of_element_located,
                                            (MobileBy.XPATH, "//*[@text='联系人']"))
        elements = self.finds(MobileBy.ID, "ddw")
        print(elements)
        return self.searcher_num, len(elements)

