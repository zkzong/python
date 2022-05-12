# author: admin
# date: 2022/5/12 14:02

'''try except语句'''
try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a / b
    print('结果是：', result)
except ZeroDivisionError:
    print('除数不能为0')
except ValueError:
    print('输入的不是整数')
print('程序正常结束')

'''try except else语句'''
try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a / b
except BaseException as e:
    print('发生了异常：', e)
else:
    print('结果是：', result)

'''try except else finally语句'''
try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a / b
except BaseException as e:
    print('发生了异常：', e)
else:
    print('结果是：', result)
finally:
    print('程序正常结束')