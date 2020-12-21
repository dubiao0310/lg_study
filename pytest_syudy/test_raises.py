# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 下午2:37
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_raises.py
import pytest


class TestRaises:

    def setup(self):
        pass


    @pytest.mark
    def test_Raises(self):

        with pytest.raises(Exception):
            assert 1==1