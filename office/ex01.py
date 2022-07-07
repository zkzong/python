import xlrd
#打开excel
data = xlrd.open_workbook('example.xlsx')
#查看文件中包含sheet的名称
data.sheet_names()
#得到第一个工作表，或者通过索引顺序或工作表名称
table = data.sheets()[0]
table = data.sheet_by_index(0)
table = data.sheet_by_name(u'Sheet1')
#获取行数和列数
nrows = table.nrows
ncols = table.ncols
print(nrows)
print(ncols)
#循环行,得到索引的列表
for rownum in range(table.nrows):
    print(table.row_values(rownum))
#单元格
cell_A1 = table.cell(0,0).value
cell_C2 = table.cell(1,2).value
print(cell_A1)
print(cell_C2)
#分别使用行列索引
cell_A1 = table.row(0)[0].value
cell_A2 = table.col(1)[0].value
print(cell_A1)
print(cell_A2)