# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 下午3:24
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_register.py
from page_object.page.main import Main


class TestRegister:
    def setup(self):
        self.main = Main()

    def test_register(self):
        assert self.main.goto_register().register()