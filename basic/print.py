# author: zong
# date: 2022/4/10 17:10

# 可以输出数字
print(520)
print(98.5)

# 可以输出字符串
print('helloworld')
print("helloworld")

# 含有运算符的表达式
print(3 + 1)

# 将数据输出文件中
# 注意点：1，所指定的盘符要存在 2，使用file=
# a+ 如果文件不存在就创建，存在就在文件内容的后面继续追加
fp = open('/Users/admin/test.txt', 'a+')
print('helloworld', file=fp)
fp.close()

# 不进行换行输出（输出内容在一行当中）
print('hello', 'world', 'Python')
