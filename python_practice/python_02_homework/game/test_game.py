import pytest

from python_practice.python_02_homework.game.tonglao import TongLao
from python_practice.python_02_homework.game.xuzu import XuZu


class TestGame():
    @pytest.mark.parametrize('name,expect',[('WYZ','师弟！！！！'),
                                            ('李秋水','呸，贱人'),
                                            ('无崖子','师弟！！！！'),
                                            ('丁春秋','叛徒！我杀了你'),
                                            ('杨过','超出识别范围')])
    def test_see_people(self,name,expect):
        tl = TongLao(1000, 200)
        result = tl.see_people(name)
        assert expect == result
    @pytest.mark.parametrize('your_hp,your_power,expect',[(1000,200,'我赢了'),(3000,200,'你赢了'),(2400,100,'平局')])
    def test_fight_zms(self,your_hp,your_power,expect):
        tl = TongLao(1000, 200)
        result = tl.fight_zms(your_hp,your_power)
        assert expect == result
    def test_xz(self):
        xz = XuZu(1000,200)
        result = xz.read()
        assert "罪过罪过" == result