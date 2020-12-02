# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 18:01
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_base.py.py
from weixin.page.app import App


class TestBase:

    def setup(self):
        self.app = App().start()


    def teardown(self):
        self.app.stop()