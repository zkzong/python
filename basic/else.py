# author: zong
# date: 2022/4/30 9:47
'''
循环中使用else语句
没有碰到break时执行else语句
'''
for item in range(3):
    pwd = input("请输入密码：")
    if pwd == '8888':
        print("密码正确！")
        break
    else:
        print("密码错误！")
else:
    print("输入错误次数超过3次，退出程序！")


a = 0
while a < 3:
    pwd = input("请输入密码：")
    if pwd == '8888':
        print("密码正确！")
        break
    else:
        print("密码错误！")
        a += 1
else:
    print("输入错误次数超过3次，退出程序！")


