# author: zong
# date: 2022/4/13 21:55

# 算术运算符
print(1 + 1)  # 加法运算
print(1 - 1)  # 减法运算
print(2 * 4)  # 乘法运算
print(1 / 2)  # 除法运算
print(11 // 2)  # 5 整除运算
print(11 % 2)  # 取余运算
print(2 ** 2)  # 表示的是2的2次方
print(2 ** 3)  # 表示的是2的3次方

print(9 // 4)  # 2
print(-9 // -4)  # 2

print(9 // -4)  # -3
print(-9 // 4)  # -3 一正一负的整数公式，向下取整

print(9 % -4)  # -3 公式 余数=被除数-除数*商 9-(-4)*(-3)=9-12=-3
print(-9 % 4)  # 3                       -9-4*(-3)=9+12=3

# 赋值运算符，运算顺序从右到左
i = 3 + 4
print(i)
a = b = c = 20  # 链式赋值
print(a, id(a))
print(b, id(b))
print(c, id(c))
print('----------支持参数赋值----------')
a = 20
a += 30  # 相当于a=a+30
print(a)
a -= 10  # 相当于a=a-10
print(a)
a *= 2  # 相当于a=a*2
print(a)
print(type(a))
a /= 3
print(a)
print(type(a))
a //= 2
print(a)
print(type(a))
a %= 3
print(a)
print('----------支持参数赋值----------')
a, b, c = 20, 30, 40
print(a, b, c)
# a, b = 20, 30, 40 # 报错，因为左右变量的个数和值的个数不对应
print('----------交换两个变量的值----------')
a, b = 10, 20
print('交换之前：', a, b)
# 交换
a, b = b, a
print('交换之后：', a, b)

# 比较运算符，比较运算符的结果为bool类型
a, b = 10, 20
print('a>b吗？', a > b)
print('a<b吗？', a < b)
print('a<=b吗？', a <= b)
print('a>=b吗？', a >= b)
print('a==b吗？', a == b)
print('a!=b吗？', a != b)

'''
一个 = 称为赋值运算符，==称为比较运算符
一个变量由三部分组成，标识符（identifier）、类型（type）和值（value）
== 比较的是值还是标识呢？比较的是值
比较对象的标识使用 is
'''
a = 10
b = 10
print(a == b)  # True 说明a和b的值相等
print(a is b)  # True 说明a和b的id标识相等
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)  # True 说明list1和list2的值相等
print(list1 is list2)  # False 说明list1和list2的id标识不相等
print(id(list1))
print(id(list2))
print(a is not b)  # False 说明a和b的id标识相等
print(list1 is not list2)  # True 说明list1和list2的id标识不相等

# 比尔运算符
a, b = 1, 2
print(a == 1 and b == 2)
print(a == 1 and b < 2)
print(a != 1 and b == 2)
print(a != 1 and b != 2)

print(a == 1 or b == 2)
print(a == 1 or b < 2)
print(a != 1 or b == 2)
print(a != 1 or b != 2)

f = True
f2 = False
print(not f)
print(not f2)

s = 'helloworld'
print('w' in s)
print('k' in s)
print('w' not in s)
print('k' not in s)

# 位运算
print(4 & 8)
print(4 | 8)
print(4 << 1)
print(4 << 2)
print(4 >> 1)
print(4 >> 2)
