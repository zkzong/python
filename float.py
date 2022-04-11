# author: zong
# date: 2022/4/11 22:04

a = 3.1415
print(a, type(a))
n1 = 1.1
n2 = 2.2
n3 = 2.1
print(n1 + n2)
print(n1 + n3)

from decimal import Decimal

print(Decimal('1.1') + Decimal('2.2'))
