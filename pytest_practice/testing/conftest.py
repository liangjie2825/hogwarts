import os
import pytest
import yaml
from pytest_practice.pythoncode.calculator import Calculator

# 获取测试数据
def get_datas():
    mydatapath = os.path.dirname(__file__) + "/datas/calculator_datas.yml"
    with open(mydatapath,encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        adddatas = mydatas['add']['datas']
        addids = mydatas['add']['myids']
        divdatas = mydatas['div']['datas']
        divids = mydatas['div']['myids']
        subdatas = mydatas['sub']['datas']
        subids = mydatas['sub']['myids']
        muldatas = mydatas['mul']['datas']
        mulids = mydatas['mul']['myids']
    return [adddatas, addids, divdatas, divids,subdatas,subids,muldatas,mulids]
#加法
@pytest.fixture(params=get_datas()[0],ids=get_datas()[1])
def get_add(request):
    return request.param
#除法
@pytest.fixture(params=get_datas()[2],ids=get_datas()[3])
def get_div(request):
    return request.param
#减法
@pytest.fixture(params=get_datas()[4],ids=get_datas()[5])
def get_sub(request):
    return request.param
@pytest.fixture(params=get_datas()[6],ids=get_datas()[7])
#乘法
def get_mul(request):
    return request.param
@pytest.fixture(scope='module')
def get_cal():
    print("\n开始测试\n")
    calc = Calculator()
    yield calc
    print("\n测试结束\n")
@pytest.fixture(scope='function',autouse=True)
def start_cal():
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split('_')[-1].split(' ')[0]
    print(f"\n开始计算{test_name}\n")
    yield
    print(f"\n{test_name}计算结束\n")