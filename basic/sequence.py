# author: admin
# date: 2022/5/1 16:27
'''不可变序列 可变序列'''
'''可变序列：列表、字典'''
lst = [10, 20, 45]
print(id(lst))
lst.append(100)
print(id(lst))

'''不可变序列：字符串、元组'''
s = 'hello'
print(id(s))
s = s + 'world'
print(id(s))
print(s)

t = (10, [20, 30], 9)
print(t)
print(type(t))
print(t[0], type(t[0]), id(t[0]))
print(t[1], type(t[1]), id(t[1]))
print(t[2], type(t[2]), id(t[2]))
'''尝试将t[1]修改为100'''
print(id(100))
# t[1] = 100 # 元组是不允许修改元素的
'''由于[20,30]是列表，而列表是可变序列，所以可以向列中添加元素，而列表的内存地址不变'''
t[1].append(100)
print(t, id(t[1]))
