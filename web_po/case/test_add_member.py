# -*- coding: utf-8 -*-
# @Time    : 2020/11/16 下午10:34
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_add_member.py
from web_po.page.index_page import IndexPage


class TestAddMember:
    def setup(self):
        self.index = IndexPage()

    def test_add_member(self):
        name = "a21"
        account = "0021"
        phonenum = "1719000021"
        add_member_page = self.index.goto_add_members()
        add_member_page.add_members(name, account, phonenum)
        result = add_member_page.get_members(name)
        assert result
