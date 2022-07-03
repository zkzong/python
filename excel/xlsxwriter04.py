import xlsxwriter


# 创建一个新Excel文件并添加工作表
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

# 展开第一栏，使正文更清楚
worksheet.set_column('A:A', 20)

# 添加一个粗体格式用于高亮单元格.
bold = workbook.add_format({'bold': True})

# 写一些简单的文字。
worksheet.write('A1', 'Hello')

# 设置文本与格式 .
worksheet.write('A2', 'World', bold)

# 写一些数字，行/列符号 .
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)
#插入图像.
worksheet.insert_image('B5', '123.png')
workbook.close()