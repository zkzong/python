# author: zong
# date: 2022/5/16 22:08

import os.path
print(os.path.abspath('.'))
print(os.path.exists('a.txt'), os.path.isfile('aa.txt'))
print(os.path.join('D:\\', 'aa.txt'))
print(os.path.split('D:\\aa.txt'))
print(os.path.splitext('aa.txt'))
print(os.path.basename('D:\\code\\python\\basic\\file\\a.txt'))
print(os.path.dirname('D:\\code\\python\\basic\\file\\a.txt'))
print(os.path.isdir('D:\\code\\python\\basic\\file\\a.txt'))


# 列出指定目录下的所有py文件
import os
path = os.getcwd()
lst = os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)

# 递归遍历所有目录和文件
import os
path = os.getcwd()
lst_files = os.walk(path)
print(lst_files)
for dirpath, dirname, filename in lst_files:
    for dir in dirname:
        print(os.path.join(dirpath, dir))
    print('---------------------------------')
    for file in filename:
        print(os.path.join(dirpath, file))
    # print(dirpath)
    # print(dirname)
    # print(filename)
    # print('---------------------------------')