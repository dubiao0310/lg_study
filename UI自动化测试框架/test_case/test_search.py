# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 16:11
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_search.py
import yaml

from UI自动化测试框架.page.app import App
from UI自动化测试框架.page.main_page import Main
import pytest

from UI自动化测试框架.test_case.test_base import TestBase


class TestSearch(TestBase):
    # def setup(self):
    #     self.app = App()

    # @pytest.mark.skip
    # @pytest.mark.parametrize("value1, value2", yaml.safe_load(open("./test_main.yaml")))
    # def test_search(self, value1, value2):
    #     self.app.start().main().goto_search()
    #     # print(value1)
    #     # print(value2)

    def test_edit(self):
        self.app.start().main().goto_edit()