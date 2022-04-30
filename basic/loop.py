# author: zong
# date: 2022/4/30 9:55
'''
输出一个三行四列的矩阵
'''
for i in range(1, 4):
    for j in range(1, 5):
        print('*', end='\t')
    print()

for i in range(1, 10):
    for j in range(1, i + 1):
        print('*', end='')
    print()

for i in range(1, 10):
    for j in range(1, i + 1):
        print(i, '*', j, '=', i * j, end='\t')
    print()
