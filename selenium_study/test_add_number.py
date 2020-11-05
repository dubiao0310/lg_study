# -*- coding: utf-8 -*-
# @Time    : 2020/11/5 上午11:55
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_add_number.py
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestAddNumber:
    def setup(self):
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_add_number(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # cookies = self.driver.get_cookies()
        # db = shelve.open("add_number_cookies")
        # db["cookie"] = cookies
        # db.close()

        db = shelve.open("add_number_cookies")
        cookies = db["cookie"]
        db.close()
        for cookie in cookies:
            if "expiry" in cookie:
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        self.driver.find_element_by_id("username").send_keys("aaa")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("1234")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("17319004321")
        self.driver.find_element_by_xpath('//*[@class="js_member_editor_form"]/div[1]/a[2]').click()
        tr_ele = self.driver.find_element(By.CSS_SELECTOR,
                                 '[class="member_colRight_memberTable_tr  member_colRight_memberTable_tr_Inactive"]:nth-child(1)')
        name = tr_ele.find_element(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)").text
        department = tr_ele.find_element(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(4)").text
        mobile = tr_ele.find_element(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(5)").text
        tr_ele.click()
        account_id = self.driver.find_element(By.CSS_SELECTOR, '[class="member_display_cover_detail_bottom"]:nth-child(3)').text
        assert name == "aaa" and department == "test" and mobile == "17319004321" and account_id == "Account ID:1234"
