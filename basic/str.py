# author: zong
# date: 2022/4/11 22:25

str1 = '人生苦短，我用Python'
str2 = "人生苦短，我用Python"
str3 = '''人生苦短，
我用Python'''
str4 = """人生苦短，
我用Python"""
print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))
print(str4, type(str4))

# 字符串的驻留机制
a = 'Python'
b = "Python"
c = '''Python'''
print(a, id(a))
print(b, id(b))
print(c, id(c))

s1 = ''
s2 = ''
print(s1 is s2)
s1 = '%'
s2 = '%'
print(s1 is s2)
s1 = 'abc%'
s2 = 'abc%'
print(s1 == s2)
print(s1 is s2)

# 字符串的查询操作
s = 'hello,hello'
print(s.index('lo'))
print(s.find('lo'))
print(s.rindex('lo'))
print(s.rfind('lo'))
# print(s.index('k'))
print(s.find('k'))
# print(s.rindex('k'))
print(s.rfind('k'))

# 字符串中的大小写转换
s = 'hello,python'
a = s.upper()
print(a, id(a))
print(s, id(s))
b = s.lower()
print(b, id(b))
print(s, id(s))
print(b == s)
print(b is s)

s2 = 'hello, Python'
print(s2.swapcase())
print(s2.title())

s = 'hello,python'
'''居中对齐'''
print(s.center(20, '*'))
'''左对齐'''
print(s.ljust(20, '*'))
print(s.ljust(10))
print(s.ljust(20))
'''右对齐'''
print(s.rjust(20, '*'))
print(s.rjust(10))
print(s.rjust(20))
'''右对齐，使用0进行填充'''
print(s.zfill(20))
print(s.zfill(10))
print('-8910'.zfill(8))

s = 'hello world Python'
lst = s.split()
print(lst)
s1 = 'hello|world|Python'
print(s1.split('|'))
print(s1.split(sep='|', maxsplit=1))

'''rsplit()从右侧开始劈分'''
print(s.split())
print(s1.split('|'))
print(s1.rsplit(sep='|', maxsplit=1))

s = 'hello,python'
print('1.', s.isidentifier())
print('2.', 'hello'.isidentifier())
print('3.', '张三_'.isidentifier())
print('4.', '张三_123'.isidentifier())

print('5.', '\t'.isspace())
print('6.', 'abc'.isalpha())
print('7.', '张三'.isalpha())
print('8.', '张三1'.isalpha())
print('9.', '123'.isdecimal())
print('10.', '123四'.isdecimal())
print('11.', 'ⅡⅡⅡ'.isdecimal())  # 罗马数字
print('12.', '123'.isnumeric())
print('13.', '123四'.isnumeric())
print('14.', 'ⅡⅡⅡ'.isnumeric())
print('15.', 'abc1'.isalnum())
print('16.', '张三123'.isalnum())
print('17.', 'abc!'.isalnum())

s = 'hello,Python'
print(s.replace('Python', 'Java'))
s1 = 'hello,Python,Python,Python'
print(s1.replace('Python', 'Java', 2))

lst = ['hello', 'Java', 'Python']
print('|'.join(lst))
print(''.join(lst))
t = ('hello', 'Java', 'Python')
print(''.join(t))

print('*'.join('Python'))

print('apple' > 'app')
print('apple' > 'banana')
print(ord('a'), ord('b'))
print(chr(97), chr(98))
print(chr(26472))

'''
==与is的区别
==比较的是value
is比较的是id
'''
a = b = 'Python'
c = 'Python'
print(a == b)
print(b == c)
print(a is b)
print(a is c)
print(id(a))
print(id(b))
print(id(c))

s = 'hello,Python'
s1 = s[:5]
s2 = s[6:]
s3 = '!'
newstr = s1 + s3 + s2
print(s1)
print(s2)
print(newstr)
print('-------------------------------')
print(id(s))
print(id(s1))
print(id(s2))
print(id(s3))
print(id(newstr))
print('-------------切片[start:end:step]------------------')
print(s[1:5:1])
print(s[::2])
print(s[::-1])
print(s[-6::1])

# 格式化字符串
# %占位符
name = '张三'
age = 20
print('我叫%s，今年%d岁' % (name, age))
# {}
print('我叫{0}，今年{1}岁'.format(name, age))
# f-string
print(f'我叫{name}，今年{age}岁')

print('%10d' % 99)  # 10表示宽度
print('%.3f' % 3.1415926)
print('%10.3f' % 3.1415926)
print('hellohello')

print('{0:.3}'.format(3.1415926))  # .3表示一共是3位数
print('{:.3f}'.format(3.1415926))  # .3f表示一共是3位小数
print('{:10.3f}'.format(3.1415926))

s = '天涯共此时'
# 编码
print(s.encode(encoding='GBK')) # 在GBK这种编码格式中，一个中文占两个字节
print(s.encode(encoding='UTF-8')) # 在UTF-8这种编码格式中，一个中文占三个字节
# 解码
byte=s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))
byte=s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))