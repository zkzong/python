# author: admin
# date: 2022/5/23 07:39
import random

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# r = random.choice(lst)
# print(r)

lst = []
for i in range(32):
    lst.append('select * from lf_user_bill_2022_'+str(i)+'')
print(lst)
print(' union '.join(lst))

# print(2**128 > 20220104140807111111162151027176084384)