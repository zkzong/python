# author: admin
# date: 2022/5/14 18:30

# 封装
class Car:
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        print('汽车已启动...')

car = Car('奥迪')
car.start()
print(car.brand)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # 年龄不希望在类的外部被使用，所以加了两个_
    def show(self):
        print(self.name, self.__age)

stu= Student('张三', 18)
stu.show()
# print(stu.__age) # 不能访问私有变量
print(dir(stu)) # 查看类的属性
print(stu._Student__age)