# -*- coding: utf-8 -*-
# @Time    : 2020/12/28 下午5:18
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_backend.py

import requests


class Test_case:

    def test_post(self):
        url = "http://127.0.0.1:5000/testcase"
        data = {
            'name': "test2",
            "des": "1234",
            "steps": "1234"
        }
        r = requests.post(url=url, json=data)
        assert r.status_code == 200

    def test_task_post(self):
        url = "http://127.0.0.1:5000/taskserver"
        data = {
            "id": 3,
            "case_list": [1, 3]
        }
        r = requests.post(url=url, json=data)
        assert r.status_code == 200

    def test_report_post(self):
        url = "http://127.0.0.1:5000/reportserver"
        data = {
            "id": 1,
            "pass_num": 2,
            "fail_num": 1,
            "task_id": 3
        }
        r = requests.post(url=url, json=data)
        assert r.status_code == 200

    def test_user_post(self):
        url = "http://127.0.0.1:5000/register"
        data = {
            "name": "zhangsan",
            "password": "1234",
        }
        r = requests.post(url=url, json=data)
        assert r.status_code == 200


