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
