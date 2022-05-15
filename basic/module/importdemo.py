# author: admin
# date: 2022/5/15 21:50

import math
print(id(math))
print(type(math))
print(math)
print(math.pi)
print('--------------------')
print(dir(math))
print(math.pow(2, 3), type(math.pow(2, 3)))
print(math.ceil(9.001))
print(math.floor(9.999))

from math import pi, pow, ceil, floor
print(pi)
print(pow(2, 3))

# 导入自定义模块
import calc
print(calc.add(1, 2))
print(calc.div(10, 2))

from calc import add, div
print(add(1, 2))