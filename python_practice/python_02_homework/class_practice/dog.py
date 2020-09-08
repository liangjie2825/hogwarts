class Dog():
    def __init__(self,breed,age,weight,color):
        self.breed = breed
        self.age = age
        self.weight = weight
        self.color = color
    def call(self):
        print("汪汪汪")
    def eat(self):
        print("狗喜欢啃骨头")