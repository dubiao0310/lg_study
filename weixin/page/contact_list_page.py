# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 17:39
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : contact_list_page.py
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from weixin.page.base_page import BasePage
from weixin.page.member_invite_page import MemberInvitePage
from weixin.page.searcher_contact_page import SearcherContactPage


class ContactList(BasePage):

    def __init__(self, driver: WebDriver = None, searcher_num=None):
        self._driver = driver
        self.searcher_num = searcher_num

    def goto_member_invite_page(self):
        self.find_by_scroll("添加成员").click()
        return MemberInvitePage(self._driver)

    def goto_searcher_contact_page(self):
        self.find(MobileBy.ID, "hk9").click()
        return SearcherContactPage(self._driver)