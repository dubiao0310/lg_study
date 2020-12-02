# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 18:00
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_contact_add.py
import yaml

from weixin.test_case.test_base import TestBase
import pytest


class TestContactAdd(TestBase):

    @pytest.mark.parametrize("name, gender, phone", yaml.safe_load(open("./add_contact.yaml")))
    def test_contact_add(self, name, gender, phone):

        result = self.app.goto_main().goto_contact().goto_member_invite_page().gotp_add_contact_apge(). \
            edit_contact(name, gender, phone).verify_toast()

        assert result == "添加成功"

