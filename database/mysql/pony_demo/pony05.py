from pony.orm import *

db = Database("mysql", host="localhost",
              user="root",
              passwd="root",
              db="test")


class Person(db.Entity):
    name = Required(str)
    age = Required(int)


sql_debug(True)  # 显示debug信息(sql语句)
db.generate_mapping(create_tables=True)  # 如果数据库表没有创建表


@db_session
def create_persons():
    p1 = Person(name="Person1", age=20)
    p2 = Person(name="Person2", age=22)
    p3 = Person(name="Person3", age=12)
    print(p1.id)  # 这里得不到id,没提交
    commit()
    print(p1.id)  # 这里得不到已经有id


create_persons()
