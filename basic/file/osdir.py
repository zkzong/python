# author: zong
# date: 2022/5/16 22:00

import os
print(os.getcwd())

lst = os.listdir('../file')
print(lst)

# os.mkdir('newdir')
# os.makedirs('A/B/C')

# os.rmdir('newdir')
# os.removedirs('A/B/C')

os.chdir('../')
print(os.getcwd())