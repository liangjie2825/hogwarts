# 测试计算器代码块
import pytest

class TestCalculator:
    @pytest.mark.add
#    @pytest.mark.run(order=0)
    @pytest.mark.first
    def test_add(self,get_cal,start_cal,get_add):
        if type(get_add[0]) is float or type(get_add[1]) is float:
            result = round(get_cal.add(get_add[0],get_add[1]),2)
        else:
            result = get_cal.add(get_add[0], get_add[1])
        assert get_add[2] == result
    @pytest.mark.div
#    @pytest.mark.run(order=3)
    @pytest.mark.fourth
    def test_div(self,get_cal,start_cal,get_div):
        # 除数为0时，程序员需要进行异常处理，结果应该为空
        if get_div[1] == 0:
            result = None
        else:
            result = round(get_cal.div(get_div[0],get_div[1]),2)
        assert get_div[2] == result
    @pytest.mark.sub
#    @pytest.mark.run(order=1)
    @pytest.mark.second
    def test_sub(self,get_cal,start_cal,get_sub):
        if type(get_sub[0]) is float or type(get_sub[1]) is float:
            result = round(get_cal.sub(get_sub[0],get_sub[1]),2)
        else:
            result = get_cal.sub(get_sub[0], get_sub[1])
        assert get_sub[2] == result
    @pytest.mark.mul
#    @pytest.mark.run(order=2)
    @pytest.mark.third
    def test_mul(self,get_cal,start_cal,get_mul):
        result = get_cal.mul(get_mul[0],get_mul[1])
        assert get_mul[2] == result

