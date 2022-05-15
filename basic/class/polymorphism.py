# author: admin
# date: 2022/5/14 19:10

# 多态
class Animal(object):
    def eat(self):
        print('动物会吃')

class Dog(Animal):
    def eat(self):
        print('狗会吃骨头')

class Cat(Animal):
    def eat(self):
        print('猫会吃鱼')

class Person:
    def eat(self):
        print('人会吃饭')

def fun(obj):
    obj.eat()

fun(Animal())
fun(Dog())
fun(Cat())
fun(Person())