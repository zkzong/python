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
print('11.', 'ⅡⅡⅡ'.isdecimal()) # 罗马数字
print('12.', '123'.isnumeric())
print('13.', '123四'.isnumeric())
print('14.', 'ⅡⅡⅡ'.isnumeric())
print('15.', 'abc1'.isalnum())
print('16.', '张三123'.isalnum())
print('17.', 'abc!'.isalnum())
