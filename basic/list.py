# author: admin
# date: 2022/4/30 11:17
a = 10
lst = ['hello', 'world', 98]
print(id(lst))
print(type(lst))
print(lst)

'''
创建列表的第一种方式，使用[]
'''
lst = ['hello', 'world', 98]
print(lst[0], lst[-3])

'''
创建列表的第二种方式，使用内置函数list
'''
lst = list(['hello', 'world', 98])

'''
index()方法，返回元素在列表中的索引
'''
lst = ['hello', 'world', 98, 'hello']
print(lst.index('hello'))
print(lst.index('hello', 2, 4))
# print(lst.index('Python'))
print(lst[2])
print(lst[-3])
# print(lst[10])

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print('原列表', id(lst))
lst2 = lst[1:6:1]
print('切片后的列表', id(lst2))
print(lst[1:6])
print(lst[1:6:])
print(lst[1:6:2])
print(lst[:6:2])
print(lst[1::2])
print('------step步长为负数的情况------')
print('原列表', lst)
print(lst[::-1])
print(lst[7::-1])
print(lst[6:0:-2])

lst = [10, 20, 'python', 'hello']
print(10 in lst)
print(100 in lst)
print(10 not in lst)
print(100 not in lst)

for item in lst:
    print(item)

'''
向列表的末尾添加元素
'''
lst = [10, 20, 30]
print('添加元素前', lst, id(lst))
lst.append(40)
print('添加元素后', lst, id(lst))
lst2 = ['hello', 'world']
lst.append(lst2)
lst.extend(lst2)
print(lst)

lst.insert(1, 90)
print(lst)

lst3 = [True, False, 'hello']
lst[1:] = lst3
print(lst)

'''
删除列表中的元素
'''
lst = [10, 20, 30, 40, 50, 60, 30]
lst.remove(30)
print(lst)
# lst.remove(100)
lst.pop(1)
print(lst)
# list.pop(5)
lst.pop()
print(lst)

print('------切片操作-删除至少一个元素，将产生一个新的列表------')
new_list = lst[1:3]
print('原列表', lst)
print('删除后的列表', new_list)
'''不产生新的列表对象，而是删除原列表中的元素'''
lst[1:3] = []
print(lst)

'''清除列表中的所有元素'''
lst.clear()
print(lst)

'''del语句将列表对象删除'''
del lst
# print(lst)

'''
修改列表中的元素
'''
lst = [10, 20, 30, 40]
lst[2] = 100
print(lst)
lst[1:3] = [200, 300, 400, 500]
print(lst)

'''排序'''
lst = [20, 40, 10, 98, 54]
print('排序前的列表', lst, id(lst))
lst.sort()
print('排序后的列表', lst, id(lst))
lst.sort(reverse=True)
print(lst)
lst.sort(reverse=False)
print(lst)
print('------使用内置函数sorted()对列表进行排序，将产生一个新的列表对象------')
lst = [20, 40, 10, 98, 54]
print('排序前的列表', lst, id(lst))
new_list = sorted(lst)
print('排序后的列表', new_list, id(new_list))
desc_list = sorted(lst, reverse=True)
print(desc_list)

'''
列表生成式
'''
lst = [i*i for i in range(1, 11)]
print(lst)
lst2 = [i*2 for i in range(1, 6)]
print(lst2)