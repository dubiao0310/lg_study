# -*- coding: utf-8 -*-
# @Time    : 2020/11/3 上午11:16
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : xpath_test.py.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXpath:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get("https://www.baidu.com")
        def wait(x):
            return len(self.driver.find_elements(By.XPATH, '//*[@class="mnav s-top-more-btn"]')) >= 1

        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="su"]')))

        self.driver.find_element(By.XPATH, '//*[@id="su"]').click()

