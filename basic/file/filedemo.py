# author: zong
# date: 2022/5/16 13:48

# 读
file = open('a.txt', 'r', encoding='utf-8')
print(file.readlines())
file.close()

# 写
file = open('b.txt', 'w')
file.write('Python')
file.close()

file = open('b.txt', 'a')
file.write('Python')
file.close()

# 二进制读写
src_file = open('git.png', 'rb')
target_file = open('git_copy.png', 'wb')
target_file.write(src_file.read())
src_file.close()
target_file.close()

# 常用方法
file = open('a.txt', 'r')
# print(file.read(2))
# print(file.readline())
print(file.readlines())

file = open('a.txt', 'a')
file.write('hello')
lst = ['java', 'go', 'python']
file.writelines(lst)
file.close()

file = open('a.txt', 'r', encoding='utf-8')
file.seek(2)
print(file.read())
print(file.tell())
file.close()