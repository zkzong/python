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