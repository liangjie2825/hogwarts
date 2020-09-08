class TongLao():
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def see_people(self, name):
        if (name == 'WYZ') | (name == '无崖子'):
            return "师弟！！！！"
        elif name == '李秋水':
            return "呸，贱人"
        elif name == '丁春秋':
            return "叛徒！我杀了你"
        else:
            return "超出识别范围"
    def fight_zms(self,your_hp,your_power):
        self.hp /= 2
        self.power *= 10
        self.hp = self.hp - your_power
        print(f"我遭到你{your_power}点伤害，剩余血量为{self.hp}")
        your_hp = your_hp - self.power
        print(f"你遭到我{self.power}点伤害，剩余血量为{your_hp}")
        if self.hp > your_hp:
            return "我赢了"
        elif self.hp < your_hp:
            return "你赢了"
        else:
            return "平局"