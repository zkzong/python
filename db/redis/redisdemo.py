# author: zong
# date: 2022/6/11 10:15

import redis
client = redis.StrictRedis(host='localhost', port=6379, password='zong', db=0)
client.lpush('zong', 'zong')
print(client.llen('zong'))
client.lpop('zong')

client.sadd('test_set', 'www.baidu.com')
url = client.spop('test_set')
length = client.scard('url')
print(url, length)