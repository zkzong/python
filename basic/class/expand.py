# author: admin
# date: 2022/5/14 19:08

# 继承
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)

class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no
    # 子类重写父类方法
    def info(self):
        super().info()
        print(self.stu_no)

class Teacher(Person):
    def __init__(self, name, age, teachofyear):
        super().__init__(name, age)
        self.teachofyear = teachofyear
    def info(self):
        super().info()
        print(self.teachofyear)

stu = Student('张三', 18, '001')
teacher = Teacher('李四', 30, '02')
stu.info()
teacher.info()


# 多继承
class A(object):
    pass
class B(object):
    pass
class C(A, B):
    pass

# object
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return 'Student object (name: %s, age: %s)' % (self.name, self.age)
stu = Student('张三', 18)
print(dir(stu))
print(stu)
print(type(stu))
