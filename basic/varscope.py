# author: admin
# date: 2022/5/8 17:00

def func(a,b):
    c=a+b
    print(c)

# print(c)
# print(a)

name='admin'
print(name)
def func2():
    print(name)

func2()

def func3():
    global age
    age=18
    print(age)

func3()
print(age)