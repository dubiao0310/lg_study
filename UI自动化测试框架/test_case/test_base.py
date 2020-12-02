# -*- coding: utf-8 -*-
# @Time    : 2020/11/19 20:25
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_base.py
from UI自动化测试框架.page.app import App


class TestBase:

    app = None
    def setup(self):
        self.app = App()