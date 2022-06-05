# author: zong
# date: 2022/6/4 9:06

import openpyxl
import datetime

wb = openpyxl.Workbook()
ws = wb.active
print(ws.title)
# 第一行第一列
ws['A1'] = 520
# 第二行
ws.append([1, 2, 3])
ws['A3'] = datetime.datetime.now()
wb.save('demo.xlsx')


# 打开excel文件
wb = openpyxl.load_workbook('豆瓣TOP250电影.xlsx')
print(type(wb))

# 获取工作表
# print(wb.get_sheet_names())
print(wb.sheetnames)
# ws = wb.get_sheet_by_name('Sheet')
ws = wb['Sheet']

# 创建和删除工作表
nws = wb.create_sheet(index=0, title='新建工作表')
print(wb.sheetnames)
wb.remove(wb['新建工作表'])
print(wb.sheetnames)

# 定位单元格
c = ws['A2']
print(c.row)
print(c.column)
print(c.coordinate)
print(ws['A2'].value)
print(c.value)
d = c.offset(2, 0)
print(d.value)

# 'AAA'是多少
print(openpyxl.cell.cell.get_column_letter(496))
print(openpyxl.utils.cell.column_index_from_string('JB'))

# 访问多个单元格
for each_movie in ws['A2':'B10']:
    for each_cell in each_movie:
        print(each_cell.value, end=' ')
    print('\n')
for each_row in ws.rows:
    print(each_row[0].value)
for each_row in ws.iter_rows(min_row=2, min_col=1, max_row=4, max_col=2):
    print(each_row[0].value)

# 拷贝工作表
new = wb.copy_worksheet(ws)
print(type(new))
wb.save('豆瓣TOP250电影.xlsx')