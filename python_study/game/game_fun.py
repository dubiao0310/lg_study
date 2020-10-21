# -*- coding: utf-8 -*-
# @Time    : 2020/10/21 下午3:48
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : game_fun.py


# 定义fight函数实现游戏逻辑
import random

def fight(enemy_hp, enemy_power):
    # 定义4个变量存放数据
    my_hp = 1000
    my_power = 200

    # 打印敌人的血量和攻击力
    print("敌人的血量为%s，攻击力为%s" % (enemy_hp, enemy_power))

    # 加入循环，让游戏可以进行多轮
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        # 判断谁的血量小于等于0
        if my_hp <= 0:
            # 打印我和敌人的剩余血量
            print("我的剩余血量为%s" % my_hp)
            print("敌人的剩余血量为%s" % enemy_power)
            print("我输了")
            # 满足条件跳出循环
            break
        elif enemy_hp <= 0:
            print("我的剩余血量为%s" % my_hp)
            print("敌人的剩余血量为%s" % enemy_power)
            print("我赢了")
            break

if __name__ == "__main__":
    # 利用列表推导式生成hp
    hp = [x for x in range(990, 1010)]
    # 随机生成敌人的血量
    enemy_hp = random.choice(hp)
    # 敌人的攻击力用randint方法生成随机整数
    enemy_power = random.randint(190, 210)
    # 调用函数，传入敌人的hp和power
    fight(enemy_hp, enemy_power)