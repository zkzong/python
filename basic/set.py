# author: admin
# date: 2022/5/2 10:09

# 集合的创建方式
'''第一种创建方式，使用{}'''
s = {2, 3, 4, 5, 5, 6, 7, 7}  # 集合中的元素不允许重复
print(s)
'''第二种创建方式，使用set()'''
s1 = set(range(6))
print(s1, type(s1))
s2 = set([1, 2, 4, 5, 5, 5, 6, 6])
print(s2, type(s2))
s3 = set((1, 2, 3, 4, 5, 65))
print(s3, type(s3))
s4 = set('Python')
print(s4, type(s4))
s5 = set({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
print(s5, type(s5))
# 空集合
s6 = {}  # dict字典类型
print(s6, type(s6))
s7 = set()
print(type(s7))

# 集合的操作
'''集合元素的判断操作'''
s = {10, 20, 30, 40, 50, 60}
print(10 in s)
print(100 in s)
print(10 not in s)
print(100 not in s)
'''集合元素的新增操作'''
s.add(70)
print(s)
s.update({200, 400, 300})
print(s)
s.update([500, 600, 700])
print(s)
'''集合元素的删除操作'''
s.remove(70)
print(s)
# s.remove(55)  # KeyError: 55
s.discard(50)
s.discard(55)
print(s)
s.pop()
# s.pop(100)
print(s)
s.clear()
print(s)

'''两个集合是否相等（元素相同，就相等）'''
s = {10, 20, 30, 40}
s2 = {30, 40, 20, 10}
print(s == s2)
print(s != s2)
'''一个集合是否是另一个集合的子集'''
s1 = {10, 20, 30, 40, 50, 60}
s2 = {10, 20, 30, 40}
s3 = {10, 20, 90}
print(s2.issubset(s1))
print(s3.issubset(s1))
'''一个集合是否是另一个集合的超集'''
print(s1.issuperset(s2))
print(s1.issuperset(s3))
'''两个集合是否没有交集'''
print(s2.isdisjoint(s3))  # False 有交集为False
s4 = {100, 200, 300}
print(s2.isdisjoint(s4))  # True 无交集为True

# 集合的数学操作
'''集合的交集'''
s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 50, 60}
print(s1.intersection(s2))
print(s1 & s2)
# print(s1)
# print(s2)
'''集合的并集'''
print(s1.union(s2))
print(s1 | s2)
# print(s1)
# print(s2)
'''集合的差集'''
print(s1.difference(s2))
print(s1 - s2)
'''集合的对称差集'''
print(s1.symmetric_difference(s2))
print(s1 ^ s2)

'''列表生成式'''
lst = [i * i for i in range(6)]
print(lst)
'''集合生成式'''
s = [i * i for i in range(10)]
print(s)
