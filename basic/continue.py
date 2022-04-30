# author: zong
# date: 2022/4/30 9:38
'''
要求输出1-50之间所有5的倍数
'''

for i in range(1, 51):
    if i % 5 == 0:
        print(i)

print('------使用continue------')
for i in range(1, 51):
    if i % 5 != 0:
        continue
    print(i)
