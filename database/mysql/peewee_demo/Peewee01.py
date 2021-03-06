from datetime import date
from peewee import *

db = SqliteDatabase('people.db')

'''模型定义'''
class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db #这个模型使用了“people.db”数据库

class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db #这个模型使用了“people.db”数据库

"""连接数据库"""
db.connect()
"""创建Person和Pet表"""
db.create_tables([Person, Pet])

uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), is_relative=True)
uncle_bob.save()

"""连接数据库关闭"""
db.close()