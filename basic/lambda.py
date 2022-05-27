# author: admin
# date: 2022/5/26 16:18

g = lambda x, y: x + y
print(g(1, 2))

# 闭包
def funX(x):
    return lambda y: x * y
temp = funX(8)
print(temp(5))