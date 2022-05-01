# author: admin
# date: 2022/5/1 16:32
'''元组的创建方式'''
'''第一种创建方式，使用()'''
t = ('Python', 'world', 98)
print(t)
print(type(t))

t2 = 'Python', 'world', 98
print(t2)
print(type(t2))

t3 = ('Python',)
print(t3)
print(type(t3))

'''第二种创建方式，使用内置函数tuple()'''
t1 = tuple(('Python', 'world', 98))
print(t1)
print(type(t1))

'''空元组'''
t4 = ()
t5 = tuple()
