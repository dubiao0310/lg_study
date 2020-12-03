# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 下午2:48
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_tag.py
import pytest
from repuests_study.base_tag import BaseTag
import json
from jsonpath import jsonpath
import yaml
import shelve
from hamcrest import *

def get_test_data():
    param = []
    tag_data = yaml.safe_load(open("./tag_data.yaml"))
    for tag_dict in tag_data:
        param.append([tag_dict['group_name'], tag_dict['tag_name']])

    return param


def get_clear_data():
    db = shelve.open("./clear_data")
    clear_data = db["clear_data"]
    return clear_data


class TestTag:
    def setup_class(self):
        self.base_tag = BaseTag()
        self.clear_list = []
        self.base_tag.del_tag(get_clear_data())

    def test_get_tag(self):
        r = self.base_tag.get_tag_list()
        assert_that(r.status_code, equal_to(200))
        assert_that(jsonpath(r.json(), "$..errcode"))

    @pytest.mark.parametrize("group_name, tag_name", get_test_data())
    def test_add_tag(self, group_name, tag_name):
        add_r = self.base_tag.add_tag(tag_name=tag_name, group_name=group_name)

        self.clear_list.extend(jsonpath(add_r.json(), "$..id"))
        db = shelve.open("clear_data")
        db["clear_data"] = self.clear_list
        db.close()

        get_r = self.base_tag.get_tag_list()
        all_tag_name = jsonpath(get_r.json(), "$..name")

        set_all_tag_name = set(all_tag_name)
        set_name = set(tag_name)

        assert_that(add_r.status_code, equal_to(200))
        assert_that(jsonpath(add_r.json(), "$..errcode")[0], equal_to(0))
        assert set_name.issubset(set_all_tag_name)

    @pytest.mark.parametrize("id, name", [[get_clear_data()[0], "edit_name"]])
    def test_edit_tag(self, id, name):

        get_r = self.base_tag.get_tag_list(id)
        edit_name = jsonpath(get_r.json(), "$..name")
        edit_r = self.base_tag.edit_tag(id, name)
        get_all_r = self.base_tag.get_tag_list()
        all_name = jsonpath(get_all_r.json(), "$..name")

        assert_that(edit_r.status_code, equal_to(200))
        assert_that(jsonpath(edit_r.json(), "$..errcode")[0], equal_to(0))
        assert edit_name not in all_name and name in all_name

    @pytest.mark.parametrize("id", [[get_clear_data()[0]]])
    def test_del_tag(self, id):
        del_r = self.base_tag.del_tag(tag_id=id)
        get_r = self.base_tag.get_tag_list()

        assert_that(del_r.status_code, equal_to(200))
        assert_that(jsonpath(del_r.json(), "$..errcode")[0], equal_to(0))
        assert id not in jsonpath(get_r.json(), "$..id")


if __name__ == '__main__':
    pytest.main(["test_tag.py", "-v"])

