# -*- coding: utf-8 -*-
# @Time    : 2020/10/26 下午8:24
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : second_task.py


class TongLao:

    def __init__(self, tl_hp, tl_power):
        """
        :param hp: 血量
        :param power: 武力值
        """
        self.tl_hp = tl_hp
        self.tl_power = tl_power

    def see_people(self, name):
        """
        :param name: 输入姓名
        :return:
        """
        if name == "wyz":
            print("师弟！！！")
        elif name == "LQS":
            print("师弟是我的")
        elif name == "DCQ":
            print("叛徒，我杀了你")
        else:
            print("who are you")

    def fight_zms(self, name, enemy_hp, enemy_power):
        """
        :param enemy_hp: 敌人血量
        :param enemy_power: 敌人武力值
        :return:
        """
        tl_hp_zms = self.tl_hp / 2
        tl_power_zms = self.tl_power * 10

        self.tl_hp = tl_hp_zms - enemy_power
        enemy_hp = enemy_hp - tl_power_zms

        if self.tl_hp > enemy_hp:
            print("TL胜")
        elif self.tl_hp < enemy_hp:
            print("%s胜" % name)
        else:
            print("平手")


if __name__ == '__main__':
    tl = TongLao(100, 6)
    tl.fight_zms("DCQ", 80, 9)