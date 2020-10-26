# -*- coding: utf-8 -*-
# @Time    : 2020/10/26 下午8:09
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : first_task.py


# 创建手机类
class Phone:

    def call(self):
        print("这是打电话")

    def information(self):
        print("这是信息")

    def camera(self):
        print("这是照相机")


# 创建耳机类
class Headset:

    def __init__(self, type):
        self.type = type

    def suspend(self):
        print("这是暂停键")

    def start(self):
        pass


if __name__ == '__main__':
    # 实例化手机对象
    phone = Phone()
    # 调用电话方法
    phone.call()