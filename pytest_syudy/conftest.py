# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 下午3:29
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_scope.py
import pytest


@pytest.fixture(scope="function", autouse=True)
def fun_scope():
    print("function")


@pytest.fixture(scope="class")
def class_scope():
    print("class")


@pytest.fixture(scope="module")
def module_scope():
    print("module")


@pytest.fixture(scope="session")
def session_scope():
    print("session")



@pytest.mark.usefixtures("fun_scope")
def test_fixture():
    print("test")



@pytest.mark.usefixtures("class_scope")
class TestClass:

    def test_a(self):
        print("test_a")