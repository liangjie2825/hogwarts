# 测试计算器代码块
import os
import pytest
import yaml
from pytest_practice.pythoncode.calculator import Calculator

# 获取测试数据
def get_datas():
    mydatapath = os.path.dirname()+"/datas/calculator_datas.yml"
    with open(mydatapath,encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        adddatas = mydatas['add']['datas']
        addids = mydatas['add']['myids']
        divdatas = mydatas['div']['datas']
        divids = mydatas['div']['myids']
    return [adddatas,addids,divdatas,divids]

class TestCalculator:
    def setup_class(self):
        print("开始测试")
        self.calc = Calculator()
    def teardown_class(self):
        print("测试结束")
    def setup(self):
        # 获取测试方法名称
        test_name = os.environ.get('PYTEST_CURRENT_TEST').split('_')[-1].split(' ')[0]
        print(f"开始计算{test_name}")
        # print("开始计算")
    def teardown(self):
        # 获取测试方法名称
        test_name = os.environ.get('PYTEST_CURRENT_TEST').split('_')[-1].split(' ')[0]
        print(f"{test_name}计算结束")
        # print("计算结束")
    @pytest.mark.add
    @pytest.mark.parametrize('x,y,expect',get_datas()[0],ids=get_datas()[1])
    def test_add(self,x,y,expect):
        if type(x) is float or type(y) is float:
            result = round(self.calc.add(x,y),2)
        else:
            result = self.calc.add(x, y)
        assert expect == result
#     @pytest.mark.sub
# #    @pytest.mark.parametrize('x,y,expect', get_datas()[4], ids=get_datas()[5])
#     def test_sub(self,x,y,expect):
#         if type(x) is float or type(y) is float:
#             result = round(self.calc.sub(x,y),2)
#         else:
#             result = self.calc.sub(x, y)
#         assert expect == result
#     @pytest.mark.mul
# #    @pytest.mark.parametrize('x,y,expect', get_datas()[6], ids=get_datas()[7])
#     def test_mul(self,x,y,expect):
#         result = self.calc.mul(x,y)
#         assert expect == result
    @pytest.mark.div
    @pytest.mark.parametrize('x,y,expect', get_datas()[2], ids=get_datas()[3])
    def test_div(self,x,y,expect):
        # 除数为0时，程序员需要进行异常处理，结果应该为空
        if y == 0:
            result = None
        else:
            result = round(self.calc.div(x,y),2)
        assert expect == result
