class Book():
    def __init__(self,title,page_number,auther):
        self.title = title
        self.page_number = page_number
        self.auther = auther
    def read(self):
        print("可以阅读")