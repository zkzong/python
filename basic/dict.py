# author: admin
# date: 2022/5/1 14:09
'''
字典的创建方式
'''
'''使用{}创建字典'''
scores = {'张三': 100, '李四': 98, '王五': 45}
print(scores)
print(type(scores))
'''第二种创建dict()'''
student = dict(name='张三', age=20, score=100)
print(student)
'''空字典'''
d = {}
print(d)

'''
获取字典的元素
'''
scores = {'张三': 100, '李四': 98, '王五': 45}
print(scores['张三'])
# print(scores['陈六'])
print(scores.get('张三'))
print(scores.get('陈六'))
print(scores.get('陈六', 99))

'''
key的判断
'''
scores = {'张三': 100, '李四': 98, '王五': 45}
print('张三' in scores)
print('张三' not in scores)

del scores['张三']
print(scores)
scores.clear()
print(scores)

scores['陈六'] = 99
print(scores)
scores['陈六'] = 100
print(scores)

scores = {'张三': 100, '李四': 98, '王五': 45}
# 获取所有的key
keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys))  # 将所有的key组成的视图转成列表
# 获取所有的value
values = scores.values()
print(values)
print(type(values))
print(list(values))
# 获取所有的key value对
items = scores.items()
print(items)
print(type(items))
print(list(items))  # 元组

# 字典元素的遍历
scores = {'张三': 100, '李四': 98, '王五': 45}
for item in scores:
    print(item, scores[item], scores.get(item))

d = {'name': '张三', 'name': '李四'}  # key不允许重复
print(d)
d = {'name': '张三', 'nickname': '张三'}
print(d)

items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 85, 100, 200]
d = {item.upper(): price for item, price in zip(items, prices)}
print(d)

# 清空字典
a = {1: 1, 2: 2, 3: 3}
b = a
print(a)
print(b)
a = {}
print(a)
print(b)

a = {1: 1, 2: 2, 3: 3}
b = a
print(a)
print(b)
a.clear()
print(a)
print(b)