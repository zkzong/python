import random
from mongoengine import *

connect('test')


class Stu(Document):
    sid = SequenceField()
    name = StringField()
    passwd = StringField()

    def introduce(self):
        print('序号:', self.sid, end=" ")
        print('姓名:', self.name, end=' ')
        print('密码:', self.passwd)

    def set_pw(self, pw):
        if pw:
            self.passwd = pw
            self.save()


src = 'abcdefghijklmnopqrstuvwxyz'


def get_str(x, y):
    str_sum = random.randint(x, y)
    astr = ''
    for i in range(str_sum):
        astr += random.choice(src)
    return astr


if __name__ == '__main__':
    print('插入一个文档:')
    stu = Stu(name='langchao', passwd='123123')
    stu.save()

    stu = Stu.objects(name='lilei').first()

    if stu:
        stu.introduce()
    print('插入多个文档')
    for i in range(3):
        Stu(name=get_str(2, 4), passwd=get_str(6, 8)).save()

    stus = Stu.objects()
    for stu in stus:
        stu.introduce()

    print('修改一个文档')
    stu = Stu.objects(name='langchao').first()
    if stu:
        stu.name = 'daxie'
        stu.save()
        stu.set_pw('bbbbbbbb')
        stu.introduce()

    print('删除一个文档')
    stu = Stu.objects(name='daxie').first()
    stu.delete()

    stus = Stu.objects()
    for stu in stus:
        stu.introduce()
