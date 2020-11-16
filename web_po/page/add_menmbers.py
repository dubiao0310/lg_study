# -*- coding: utf-8 -*-
# @Time    : 2020/11/16 下午2:31
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : add_menmbers.py
from selenium.webdriver.common.by import By

from web_po.page.base import Base


class AddMembers(Base):

    def add_members(self, name, account, phonenum):
        self.find(By.ID, "username").send_keys(name)
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        self.find(By.ID, "memberAdd_phone").send_keys(phonenum)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()

    def get_members(self, value):
        locator = (By.CSS_SELECTOR, "ww_checkbox")
        self.wait_click(locator)
        titles_total = []
        while True:
            elements = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
            titles = [element.get_attribute("title") for element in elements]
            if value in titles:
                return True
            titles_total.extend(titles)
            page = self.finds(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
            num, total = page.split("/", 1)
            if int(num) == int(total):
                return False
            else:
                self.find(By.CSS_SELECTOR, ".ww_commonImg ww_commonImg_PageNavArrowRightNormal").click()





