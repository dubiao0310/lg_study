# -*- coding: utf-8 -*-
# @Time    : 2020/10/21 下午3:41
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : game_round1.py

"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，
hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""


# 定义fight函数实现游戏逻辑
def fight():
    # 定义4个变量存放数据
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 200

    # 定义最终血量计算方式
    my_final_hp = my_hp - enemy_power
    enemy_final_hp = enemy_hp - my_power

    # 判断输赢
    # 三目运算，等同于的if-else，只是语法简洁一些
    print("我赢了") if my_final_hp > enemy_final_hp else print("我输了")


if __name__ == '__main__':
    fight()