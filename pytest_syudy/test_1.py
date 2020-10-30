# -*- coding: utf-8 -*-
# @Time    : 2020/10/29 下午2:41
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_1.py
import pytest


def inc(x):
    return x + 1

@pytest.mark.parametrize('a,b', [
    (1, 2),
    (3, 4)
])
def test_answer(a, b):
    assert inc(a) == b

@pytest.fixture()
def login():
    username = "kkkkk"
    print("登录操作")
    return username


class TestDome:

    def test_1(self, login):
        print("a %s" % login)

    def test_2(self):
        print("b")

    def test_3(self, login):
        print("c %s" % login)


if __name__ == '__main__':
    pytest.main(["test_1.py::TestDome::test_2", "-v"])