# author: admin
# date: 2022/5/5 22:15

def calc(a, b):
    c = a + b
    return c


result = calc(10, 20)
print(result)
result = calc(b=10, a=20)
print(result)


def fun(arg1, arg2):
    print('arg1', arg1)
    print('arg2', arg2)
    arg1 = 100
    arg2.append(10)
    print('arg1', arg1)
    print('arg2', arg2)


n1 = 11
n2 = [22, 33, 44]
print('n1', n1)
print('n2', n2)
fun(n1, n2)
print('n1', n1)
print('n2', n2)
'''
在函数调用过程中，进行参数的传递
如果是不可变对象，在函数体的修改不会影响实参的值
如果是可变对象，在函数体的修改会影响到实参的值
'''

print(bool(0))
print(bool(8))


def fun(num):
    odd = []
    even = []
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


lst = [10, 29, 34, 23, 44, 53, 55]
print(fun(lst))
'''
函数的返回值
（1）如果函数没有返回值【函数执行完毕之后，不需要给调用处提供数据】return可以省略不写
（2）函数的返回值，如果是1个，直接返回类型
（3）函数的返回值，如果是多个，返回的结果为元组
'''


def fun1():
    print('hello')
    # return


fun1()


def fun2():
    return 'hello'


res = fun2()
print(res)


def fun3():
    return 'hello', 'world'


print(fun3())

'''
函数在定义时，是否需要返回值，视情况而定
'''


def fun(a, b=10):
    print(a, b)


fun(100)
fun(20, 30)

print('hello', end='\t')
print('world')


def fun(*args):
    print(args)
    print(args[0])


fun(10)
fun(10, 20)
fun(10, 20, 30)


def fun1(**args):
    print(args)


fun1(a=10)
fun1(a=10, b=20)

print('hello', 'world', 'java', sep='-')

'''
def fun2(*args, *a):
    pass
以上代码，程序会报错，个数可变的位置参数，只能是1个
def fun2(**args, **args2):
    pass
以上代码，程序会报错，个数可变的关键字参数，只能是1个
'''


def fun2(*args1, **args2):
    pass


'''
def fun3(**args1, *args2):
    pass
在一个函数的定义过程中，既有个数可变的关键字形参，也有个数可变的位置形参，要求，个数可变的位置形参必须在个数可变的关键字形参之前
'''


def fun(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


fun(10, 20, 30)
lst = [11, 22, 33]
fun(*lst)  # 在函数调用时，将列表中的每个元素都转换为位置实参传入

fun(a=100, c=300, b=200)

dic = {'a': 100, 'b': 200, 'c': 300}
fun(**dic)  # 在函数调用时，将字典中的每个键值对都转换为关键字实参传入


def fun(a, b, c, d):
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)


fun(10, 20, 30, 40)
fun(a=10, b=20, c=30, d=40)
fun(10, 20, c=30, d=40)
'''需求：c,d只能采用关键字实参传递'''
def fun(a, b, * c, d): # 从*之后的参数，在函数调用时，只能采用关键字参数传递
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)
fun(a=10, b=20, c=30, d=40)
fun(10, 20, c=30, d=40)