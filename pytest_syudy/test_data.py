# -*- coding: utf-8 -*-
# @Time    : 2020/10/29 下午3:30
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_data.py
import pytest
import yaml


class TestData:
    @pytest.mark.parametrize("a, b", yaml.safe_load(open("./data.yaml")))
    def test_data(self,a, b):
        print(a+b)