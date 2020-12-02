# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 17:49
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : member_invite_page.py
from appium.webdriver.common.mobileby import MobileBy


from weixin.page.base_page import BasePage


class MemberInvitePage(BasePage):

    def gotp_add_contact_apge(self):
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 解决循环引用问题
        from weixin.page.add_contact_page import AddContactPage
        return AddContactPage(self._driver)


    def verify_toast(self):
        # result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        result = self.get_toast_text()
        return result