# -*- coding: utf-8 -*-
# @Time    : 2020/12/18 21:29
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_jenkins.py

import allure
import os

from selenium.webdriver.chrome.options import Options
from selenium import webdriver


@allure.feature("测试百度ui")
class TestBaidu:

    def setup(self):

        try:
            using_headless = os.environ["using_headless"]
        except KeyError:
            using_headless = None

        chrome_options = Options()
        if using_headless is not None and using_headless.lower() == "true":
            chrome_options.add_argument("--headless")

        self.driver = webdriver.Chrome(options=chrome_options)


    def teardown(self):
        self.driver.quit()


    def test_1(self):
        self.driver.get("https://www.baidu.com")

