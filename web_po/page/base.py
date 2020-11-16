# -*- coding: utf-8 -*-
# @Time    : 2020/11/16 下午1:37
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : base.py
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    _url = ""
    def __init__(self, driver:WebDriver=None):
        if driver == None:
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=option)

        else:
            self.driver = driver

        if self._url != "":
            self.driver.get(self._url)
        self.driver.implicitly_wait(5)
    def find(self, by, location):
        return self.driver.find_element(by, location)

    def finds(self, by, location):
        return self.driver.find_elements(by, location)

    def wait_click(self, location, timeout=10):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(location))



if __name__ == '__main__':
    b = Base()


