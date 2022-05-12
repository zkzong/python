# author: admin
# date: 2022/5/12 15:39
class Student:
    # 类变量
    native_place = 'China'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
    def eat(self):
        print('吃饭')

    # 静态方法
    @staticmethod
    def method():
        print('静态方法')

    # 类方法
    @classmethod
    def class_method(cls):
        print('类方法')

print(id(Student))
print(type(Student))
print(Student)

stu = Student('张三', 18)
print(id(stu))
print(type(stu))
print(stu)
stu.eat()
print(stu.name)
print(stu.age)

Student.eat(stu)

print(Student.native_place)
stu1 = Student('张三', 20)
stu2 = Student('李四', 21)
print(stu1.native_place)
print(stu2.native_place)
Student.native_place = 'USA'
print(stu1.native_place)
print(stu2.native_place)

print('-------------------------类方法的使用方式----------------------------')
Student.class_method()
print('-------------------------静态方法的使用方式----------------------------')
Student.method()