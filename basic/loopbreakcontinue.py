# author: zong
# date: 2022/4/30 10:06
'''
流程控制语句break与continue在二重循环中的使用
'''
for i in range(5):
    for j in range(1, 11):
        if j % 2 == 0:
            break
        print(j)

for i in range(5):
    for j in range(1, 11):
        if j % 2 == 0:
            continue
        print(j, end='\t')
    print()