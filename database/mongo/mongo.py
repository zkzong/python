# author: admin
# date: 2022/6/11 00:10

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

# 初始化数据库和集合的两种方式
# 1
database = client.python
collection = database.spider
# 2
database = client['python']
collection = database['spider']

# 插入数据
data = {'id': 123, 'name': 'zong', 'age': 22, 'salary': 999999}
# collection.insert_one(data)

more_data = [
    {'id': 2, 'name': '张三', 'age': 10, 'salary': 0},
    {'id': 3, 'name': '李四', 'age': 30, 'salary': -100},
    {'id': 4, 'name': '王五', 'age': 40, 'salary': 1000},
    {'id': 5, 'name': '外国人', 'age': 50, 'salary': '未知'},
    {'id': 6, 'name': '火星人', 'age': 29, 'salary': '未知'}
]
# collection.insert_many(more_data)

# 普通查找
content = collection.find()
for item in content:
    print(item)
content = collection.find({'age': 29})
for item in content:
    print(item)
# 只显示name和salary字段
content = collection.find({'age': 29}, {'_id': 0, 'name': 1, 'salary': 1})
for item in content:
    print(item)
content = [x for x in collection.find({'age': 29}, {'_id': 0, 'name': 1, 'salary': 1})]
print(content)

# 逻辑查询
# 查询所有age > 29的记录
content = collection.find({'age': {'$gt': 29}})
for item in content:
    print(item)

content = collection.find({'age': {'$gte': 29, '$lte': 40}})

content = collection.find({'salary': {'$ne': 29}})

# 对查询结果排序
content = collection.find({'age': {'$gte': 29, '$lte': 40}}).sort('age', -1)
for item in content:
    print(item)
content = collection.find({'age': {'$gte': 29, '$lte': 40}}).sort('age', 1)
for item in content:
    print(item)

# 更新记录
collection.update_one({'age': 20}, {'$set': {'name': 'king'}})
collection.update_many({'age': 20}, {'$set': {'age': 30}})

# 删除记录
collection.delete_one({'name': 'king'})
collection.delete_many({'name': 'king'})

# 对查询结果去重
content = collection.distinct('age')
print(content)