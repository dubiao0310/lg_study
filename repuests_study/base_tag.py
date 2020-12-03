# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 下午9:51
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : base_tag.py
import requests
import json
from jsonpath import jsonpath


def make_tag(tag_name, **kwargs):
    tag = []
    if isinstance(tag_name, list):
        for index, name in enumerate(tag_name):
            if "tag_order" in kwargs:
                tag.append({"name": name, "order": kwargs["tag_order"][index]})
            else:
                tag.append({"name": name})
    else:
        if "tag_order" in kwargs:
            tag.append({"name": tag_name, "order": kwargs["tag_order"][0]})
        else:
            tag.append({"name": tag_name})
    return tag


class BaseTag:
    token = ""

    def __init__(self):
        param = {
            "corpid": "wwcc131c38a6ada233",
            "corpsecret": "kbIKNQKl1Cp6kWwdUlL4_v2_wrcuzb6moqsJ-aWu2rs"
        }
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=param)
        if r.status_code == 200 and r.json()['errcode'] == 0:
            self.token = r.json()["access_token"]
        else:
            print("get token error msg: %s" % r.json()["errmsg"])

        self.param = {"access_token": self.token}

    def get_tag_list(self, tag_id_list=None):
        """
        :param tag_id_list: []
        :return: []
        """
        data = {
            "tag_id": tag_id_list
        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
                          params=self.param, json=data)

        # 结构化输出json数据
        # print(json.dumps(r.json(), indent=2))
        # return jsonpath(r.json(), "$..name")
        return r

    def add_tag(self, tag_name, **kwargs):
        """
        :param tag_name: [] or str
        :param kwargs: group_name, group_id, tag_order=[], group_order
        :return:
        """
        data = {}
        if "group_id" in kwargs:
            tag = make_tag(tag_name, **kwargs)
            data = {"group_id": kwargs["group_id"], "tag": tag}

        elif "group_name" in kwargs:
            tag = make_tag(tag_name, **kwargs)
            if "group_order" in kwargs:
                data = {"group_name": kwargs["group_name"], "order": kwargs["group_order"], "tag": tag}
            else:
                data = {"group_name": kwargs["group_name"], "tag": tag}

        else:
            print("must have group_id or group_name")
        # print(data)
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag", params=self.param,
                          json=data)
        # print(json.dumps(r.json(), indent=2))
        return r

    def edit_tag(self, id, name=None, order=None):
        """
        :param id: str
        :param name: str
        :param order: int
        :return:
        """
        data = {
            'id': id,
            "name": name,
            "order": order
        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag", params=self.param,
                          json=data)
        # print(json.dumps(r.json(), indent=2))
        return r

    def del_tag(self, tag_id=None, group_id=None):
        """
        :param tag_id: []
        :param group_id: []
        :return:
        """
        data = {
            "tag_id": tag_id,
            "group_id": group_id
        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag", params=self.param,
                          json=data)
        # print(json.dumps(r.json(), indent=2))
        return r


if __name__ == '__main__':
    b = BaseTag()
    # b.get_tag_list()
    b.add_tag([44, 222], group_name="lagou5")
    # b.edit_tag("ethq0LEAAAML7nKmllTrbHKvGzh_TwgA", "lagou")
    # b.del_tag(["ethq0LEAAAz9AF0cIzALiD2VxpVYlz7Q"])
