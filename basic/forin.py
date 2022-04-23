# author: zong
# date: 2022/4/23 18:10

for item in 'Python':
    print(item)

for i in range(10):
    print(i)

# 如果在循环体中不需要使用到自定义变量，可将自定义变量写为“_”
for _ in range(5):
    print('人生苦短，我用Python')

print('使用for循环，计算1-100之间的偶数和')
sum = 0
for item in range(1, 101):
    if item % 2 == 0:
        sum += item
print('1到100之间的偶数和为：', sum)

'''
输出100到999之间的水仙花数
举例：153 = 1*1*1 + 5*5*5 + 3*3*3
'''
for item in range(100, 1000):
    ge = item % 10
    shi = item // 10 % 10
    bai = item // 100
    # print(bai, shi, ge)
    if item == bai ** 3 + shi ** 3 + ge ** 3:
        print(item)