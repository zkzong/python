# author: zong
# date: 2022/4/23 17:52

a = 1
while a < 10:
    print(a)
    a += 1

sum = 0
a = 0
while a < 5:
    sum += a
    a += 1
print('和为', sum)

sum = 0
a = 1
while a <= 100:
    # if not bool(a % 2):
    if a % 2 == 0:
        sum += a
    a += 1
print('1-100之间的偶数和', sum)
