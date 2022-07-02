from pony.orm import *
from decimal import Decimal

db = Database("mysql", host="localhost",
              user="root",
              passwd="root",
              db="test")
db.drop_table("person", with_all_data=True)


class Person(db.Entity):
    _discriminator_ = 1  # 刻
    name = Required(str)
    age = Required(int)


class Student(Person):
    _discriminator_ = 3
    gpa = Optional(Decimal)
    mentor = Optional("Professor")


class Professor(Person):
    _discriminator_ = 2
    degree = Required(str)
    students = Set("Student")


sql_debug(True)  # 显示debug信息(sql语句)
db.generate_mapping(create_tables=True)  # 如果数据库表没有创建表


# @db_session
# def create_persons():
#     p1 = Person(name="Person", age=20)
#     s = Student(name="Student", age=22, gpa=1.2)
# 也可以Professor添加Student
#     p2 = Professor(name="Professor", age=12, degree="aaaaaa", students=[s])
#     commit()

@db_session
def create_persons():
    p1 = Person(name="Person", age=20)
    s = Student(name="Student", age=22, gpa=1.2)
    p2 = Professor(name="Professor", age=12, degree="aaaaaa", students=[s])
    commit()


create_persons()
