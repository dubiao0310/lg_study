# -*- coding: utf-8 -*-
# @Time    : 2020/10/26 下午8:45
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : xuzhu_class.py

from python_study.class_study.tl_class import TongLao


class XuZgu(TongLao):

    def read(self):
        """
        :return:
        """
        print("罪过罪过")


if __name__ == '__main__':
    xz = XuZgu(120, 9)
