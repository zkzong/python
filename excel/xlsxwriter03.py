import xlsxwriter

# 建文件及sheet.
workbook = xlsxwriter.Workbook('Expenses03.xlsx')
worksheet = workbook.add_worksheet()
# 设置粗体，默认是False
bold = workbook.add_format({'bold': True})
# 定义数字格式
money = workbook.add_format({'num_format': '$#,##0'})
#带自定义粗体blod格式写表头
worksheet.write('A1', 'Item', bold)
worksheet.write('B1', 'Cost', bold)
#写入表中的数据.
expenses = (
['Rent', 1000],
['Gas',   100],
['Food',  300],
['Gym',    50],
 )

#从标题下面的第一个单元格开始 .
row = 1
col = 0

# 迭代数据并逐行地写出它
for item, cost in (expenses):
     worksheet.write(row, col,     item)    # 带默认格式写入
     worksheet.write(row, col + 1, cost, money)  # 带自定义money格式写入
     row += 1

 # 用公式计算总数 .
worksheet.write(row, 0, 'Total',       bold)
worksheet.write(row, 1, '=SUM(B2:B5)', money)

workbook.close()