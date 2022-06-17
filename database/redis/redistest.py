# author: zong
# date: 2022/6/15 22:31
import redis

r = redis.Redis(host='localhost', port=6379, password='zong', db=0)
r.set('name', 'zong')
print(r.get('name'))

# 连接池
pool = redis.ConnectionPool(host='localhost', port=6379, password='zong')
r = redis.Redis(connection_pool=pool)
r.set('name', 'zong')
print(r.get('name'))