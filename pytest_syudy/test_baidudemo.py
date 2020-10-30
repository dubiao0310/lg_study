# -*- coding: utf-8 -*-
# @Time    : 2020/10/30 下午8:16
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_baidudemo.py


import allure
import pytest
from selenium import webdriver
import time


@allure.testcase("http:wwww.baidu.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize("test_data", ['allure', 'pytest', 'unittest'])
def test_steps_demo(test_data):

    with allure.step("打开百度首页"):
        driver = webdriver.Chrome('/home/ubuntu/Downloads/chromedriver')
        driver.get("http://www.baidu.com")
        driver.maximize_window()

    with allure.step("输入搜索词%s" % test_data):
        driver.find_element_by_id('kw').send_keys(test_data)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(1)

    with allure.step("保存图片"):
        driver.save_screenshot('./img.png')
        allure.attach.file("./img.png", attachment_type=allure.attachment_type.PNG)

    with allure.step("关闭浏览器"):
        driver.quit()
