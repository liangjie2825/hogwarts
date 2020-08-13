# 计算器代码块
class Calculator:
    def add(self,a,b):
        return a + b
    def sub(self,a,b):
        return a - b
    def mul(self,a,b):
        return a * b
    def div(self,a,b):
        try:
            result = a / b
        except ZeroDivisionError:
            print("除数不能为零")
        else:
            return result
