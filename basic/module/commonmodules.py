# author: zong
# date: 2022/5/15 22:42

import sys
print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

import time
print(time.time())
print(time.localtime(time.time()))

import urllib.request
print(urllib.request.urlopen('http://www.baidu.com').read())

import math
print(math.pi)

import schedule
def job():
    print('I am job')

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

