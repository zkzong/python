# author: zong
# date: 2022/4/11 22:36

name = '张三'
age = 20

print(type(name), type(age))  # 说明name与age的数据类型不相同
print('我叫' + name + ' 今年' + age + '岁') # 当将str类型与int类型进行连接时，报错，解决方案：类型转换
print('我叫' + name + ' 今年' + str(age) + '岁') # 将int类型通过str()函数转成了str类型
