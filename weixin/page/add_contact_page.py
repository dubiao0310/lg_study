
# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 17:44
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : add_contact_page.py
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from weixin.page.base_page import BasePage
from weixin.page.member_invite_page import MemberInvitePage


class AddContactPage(BasePage):

    def edit_contact(self, name, gender, phone):
        '''
        编辑成员信息
        '''
        self.find(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(
            name)
        self.find(MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']").click()
        if gender == "男":
            WebDriverWait(self._driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
            self.find(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.find(MobileBy.XPATH, "//*[@text='女']").click()

        self.find(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phone)
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()

        return MemberInvitePage(self._driver)
