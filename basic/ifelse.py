# author: zong
# date: 2022/4/20 22:23
money = 1000
s = int(input('请输入取款金额：'))
if money >= s:
    money = money - s
    print('取款成功，余额为：', money)

num = int(input('请输入一个整数：'))
if num % 2 == 0:
    print(num, '是偶数')
else:
    print(num, '是奇数')

score = int(input('请输入成绩：'))
if score >= 90 and score <= 100:
    print('A')
elif score >= 80 and score < 90:
    print('B')
elif score >= 70 and score < 80:
    print('C')
elif score >= 60 and score < 70:
    print('D')
elif score >= 0 and score < 60:
    print('E')
else:
    print('请输入0-100的数字')

answer = input('您是会员吗？y/n')
money = float(input('请输入您的购物金额：'))
if answer == 'y':
    if money >= 200:
        print('付款金额为：', money * 0.8)
    elif money >= 100:
        print('付款金额为：', money * 0.9)
    else:
        print('付款金额为：', money)
else:
    if money >= 200:
        print('付款金额为：', money * 0.95)
    else:
        print('付款金额为：', money)

# 条件表达式
# 从键盘录入两个整数，比较两个整数的大小
num_a = int(input('请输入第一个整数：'))
num_b = int(input('请输入第二个整数：'))
'''
if num_a > num_b:
    print(num_a, '大于等于', num_b)
else:
    print(num_a, '小于', num_b)
'''
print('使用条件表达式')
print(str(num_a) + '大于等于' + str(num_b) if num_a > num_b else str(num_a) + '小于' + str(num_b))