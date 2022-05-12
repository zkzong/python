# author: admin
# date: 2022/5/12 21:01

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating" % self.name)

stu1 = Student("张三", 20)
stu2 = Student("李四", 21)
