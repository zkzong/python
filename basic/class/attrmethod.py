# author: admin
# date: 2022/5/15 10:03

print(dir(object))


class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class D(A):
    pass


# 创建C类的对象
c = C('Jack', 20)  # c是C类型的一个实例对象
print(c.__dict__)  # 实例对象的属性字典
print(C.__dict__)

print(c.__class__)  # <class '__main__.C'> 输出对象所属的类
print(C.__bases__)  # C类的父类，元组类型
print(C.__base__)  # A类
print(C.__mro__)  # 类的层次结构，元组类型
print(A.__subclasses__())  # 输出A类的所有子类

print('-----------------')
a = 20
b = 100
c = a + b
d = a.__add__(b)
print(c)
print(d)


class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + other.name
    def __len__(self):
        return len(self.name)


stu1 = Student('Jack')
stu2 = Student('Tom')
s = stu1 + stu2
print(s)
s = stu1.__add__(stu2)
print(s)

lst = [11, 22, 32, 44]
print(len(lst))
print(lst.__len__())

print(len(stu1))

# __new__ __init__
class Person(object):

    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建的对象的id值为{0}'.format(id(obj)))
        return obj

    def __init__(self, name, age):
        print('__init__被调用执行了，self的id值为{0}'.format(id(self)))
        self.name = name
        self.age = age

print('object类的id值为{0}'.format(id(object)))
print('Person类的id值为{0}'.format(id(Person)))

# 创建Person类的实例对象
p1 = Person('Jack', 20)
print('p1的id值为{0}'.format(id(p1)))
