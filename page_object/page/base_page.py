# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 下午2:51
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : base_page.py

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""

    # :WebDriver 标记driver类型
    def __init__(self, driver:WebDriver=None):
        self._driver = ""
        if driver is None:
            self._driver = webdriver.Chrome() # 初始化第一个driver
        else:
            self._driver = driver  # 复用已有的driver

        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)