import tablib
headers = ('area', 'user', 'recharge')
data = [
    ('1', 'Rooney', 20),
    ('2', 'John', 30),
]
data = tablib.Dataset(*data, headers=headers)

#然后就可以通过下面这种方式得到各种格式的数据了。
print(data.csv)
print(data.html)
print(data.xls)
print(data.ods)
print(data.json)
print(data.yaml)
print(data.tsv)

#增加行
data.append(['3', 'Keven',18])
#增加列
data.append_col([22, 20,13], header='Age')
print(data.csv)

#删除行
del data[1:3]
#删除列
del data['Age']
print(data.csv)
