'''
一个多回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
'''
from random import randint
#定义一个游戏角色类，有hp和power两个属性
class Person():
    def __init__(self,hp,power):
        self.hp = hp
        self.power = power

def fight():
    #创建一个hp为1000，power为200的实例游戏角色me
    me = Person(1000,200)
    #创建一个hp为1000，power为200的实例游戏角色enemy
    enemy = Person(1000,200)
    while True:
        #me的攻击力
        me.power = randint(10, 50)
        #enemy的攻击力
        enemy.power = randint(0, 60)
        #回合后，me的剩余血量
        me.hp = me.hp - enemy.power
        print(f"这个回合我受到{enemy.power}点攻击，剩余血量为{me.hp}")
        #回合后，enemy的剩余血量
        enemy.hp = enemy.hp - me.power
        #当me的血量大于0，打印enemy回合的信息，否则则不打印
        if me.hp > 0:
            print(f"这个回合你受到{me.power}点攻击，剩余血量为{enemy.hp}")
        #当me的血量小于等于0时，提示我输了并跳出循环
        if me.hp <= 0:
            print("我输了")
            break
        # 当enemy的血量小于等于0时，提示你输了并跳出循环
        elif enemy.hp <= 0:
            print("你输了")
            break
fight()