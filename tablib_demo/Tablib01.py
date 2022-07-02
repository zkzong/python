import tablib

names = ['Kenneth Reitz', 'Bessie Monke']
data = tablib.Dataset()
for name in names:
    fname, lname = name.split()
    data.append([fname, lname])

data.headers = ['First Name', 'Last Name']
data.append_col([22, 20], header='Age')
# 显示某条数据信息
print(data[0])
# 显示某列的值
print(data['First Name'])
# 使用索引访问列
print(data.headers)
print(data.get_col(1))
# 计算平均年龄
ages = data['Age']
print(float(sum(ages)) / len(ages))
