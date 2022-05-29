# author: admin
# date: 2022/5/29 15:22

pwd = input("支付宝支付密码：")
if pwd.isdigit():
    print("支付数字合法")
else:
    print("支付数字不合法")

print('支付数字合法') if pwd.isdigit() else print('支付数字不合法')