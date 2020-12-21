# -*- coding: utf-8 -*-
# @Time    : 2020/12/7 上午10:19
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : ｓｔｕｄｙ.py

import requests
from requests.auth import HTTPBasicAuth
from selenium import webdriver
from jsonschema import validate
import genson
import json

# auth练习

r = requests.get("http://httpbin.testing-studio.com/basic-auth/du/123", auth=HTTPBasicAuth(username="du", password=123))
print(r.text)

# proxies
proxies = {
  "http": "http://127.0.0.1:8888",
  "https": "https://127.0.0.1:8888"
}
r = requests.get("https://www.baidu.com", proxies=proxies, verify=False)
print(r.text)


# # Schema json验证练习
# builder = genson.SchemaBuilder()
# reponse = {"name": "du", "password": [1, 2]}
# data2 = {"name": "dubiao", "password": [1, 2, 3]}
#
# with open("data1.txt", "w") as f:
#     json.dump(reponse, f)
#
# b1 = genson.SchemaBuilder()
# b1.add_schema({"type": "object", "properties": {}})
# with open("data1.txt", "r") as f2:
#     data1 = json.load(f2)
#     b1.add_object(data1)
#
#
# b2 = genson.SchemaBuilder()
# b2.add_schema({"type": "object", "properties": {}})
# b2.add_object(data2)
#
# print(b1 == b2)