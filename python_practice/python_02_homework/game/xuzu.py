from python_practice.python_02_homework.game.tonglao import TongLao

class XuZu(TongLao):
    def __init__(self,hp,power):
        super().__init__(hp,power)
    def read(self):
        return "罪过罪过"