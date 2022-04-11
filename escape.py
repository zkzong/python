# author: zong
# date: 2022/4/10 17:15

# 转义字符
print('hello\nworld')
print('hello\tworld') # 中间三个空格
print('helloooo\tworld') # 中间四个空格
print('helloooo\rworld')
print('hello\bworld')

print('http:\\\\www.baidu.com')
print('老实说：\'大家好\'')

# 原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r或R
print(r'hello\nworld')
# 注意事项：最后一个字符不能是反斜杠
# print(r'hello\nworld\')
print(r'hello\nworld\\')