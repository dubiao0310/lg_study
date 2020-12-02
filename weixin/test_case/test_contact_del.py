# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 21:48
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_contact_del.py
from weixin.test_case.test_base import TestBase


class TestContactDel(TestBase):

    def test_contact_del(self):
        first_num, second_num = self.app.goto_main().goto_contact().goto_searcher_contact_page().goto_person_info_page("a") \
            .goto_person_operation_page().goto_edit_contact_page().goto_searcher_contact_page().get_elements()
        assert first_num - 1 == second_num