import tablib
import os

#创建dataset，方法1
dataset1 = tablib.Dataset()
header1 = ('ID', 'Name', 'Tel', 'Age')
dataset1.headers = header1
dataset1.append([1, 'zhangsan', 13711111111, 16])
dataset1.append([2, 'lisi',     13811111111, 18])
dataset1.append([3, 'wangwu',   13911111111, 20])
dataset1.append([4, 'zhaoliu',  15811111111, 25])
print('dataset1:', os.linesep, dataset1, os.linesep)

#创建dataset，方法2
header2 = ('ID', 'Name', 'Tel', 'Age')
data2 = [
    [1, 'zhangsan', 13711111111, 16],
    [2, 'lisi',     13811111111, 18],
    [3, 'wangwu',   13911111111, 20],
    [4, 'zhaoliu',  15811111111, 25]
]
dataset2 = tablib.Dataset(*data2, headers = header2)
print('dataset2: ', os.linesep, dataset2, os.linesep)

#增加行
dataset1.append([5, 'sunqi', 15911111111, 30])      #添加到最后一行的下面
dataset1.insert(0, [0, 'liuyi', 18211111111, 35])   #在指定位置添加行
print('增加行后的dataset1: ', os.linesep, dataset1, os.linesep)

#删除行
dataset1.pop()      #删除最后一行
dataset1.lpop()     #删除第一行
del dataset1[0:2]   #删除第[0,2)行数据
print('删除行后的dataset1:', os.linesep, dataset1, os.linesep)

#增加列
#现在dataset1就剩两行数据了
dataset1.append_col(('beijing', 'shenzhen'), header='city')     #增加列到最后一列
dataset1.insert_col(2, ('male', 'female'), header='sex')        #在指定位置添加列
print('增加列后的dataset1: ', os.linesep, dataset1, os.linesep)

#删除列
del dataset1['Tel']
print('删除列后的dataset1: ', os.linesep, dataset1, os.linesep)


#获取各种格式的数据
print('yaml format: ', os.linesep ,dataset1.yaml, os.linesep)
print('csv format: ' , os.linesep ,dataset1.csv , os.linesep)
print('tsv format: ' , os.linesep ,dataset1.tsv , os.linesep)


#导出到Excel表格中
dataset1.title = 'dataset1'     #设置Excel中表单的名称
dataset2.title = 'dataset2'
myfile = open('mydata.xls', 'wb')
myfile.write(dataset1.xls)
myfile.close()

#如果有多个sheet表单，使用DataBook就可以了
myDataBook = tablib.Databook((dataset1, dataset2))
myfile = open(myfile.name, 'wb')
myfile.write(myDataBook.xls)
myfile.close()
