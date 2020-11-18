# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 15:14
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : base_page.py
import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    _black_list = [(By.ID, "iv_close")]
    def __init__(self, driver:WebDriver=None):
        self._dirver = driver


    def find(self, by, locator):
        try:
            element = self._dirver.find_element(by, locator)
            return element
        except:
            for black in self._black_list:
                elements = self._dirver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    break
            # 处理完黑名单后再次查找原来的内容
            return self.find(by, locator)


    def steps(self, path):
        with open(path) as f:
            steps = yaml.safe_load(f)
        element = None
        for step in steps:
            if "by" in step.keys():
                element = self.find(step["by"], step["locator"])
            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    element.click()