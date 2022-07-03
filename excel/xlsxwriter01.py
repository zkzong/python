import xlsxwriter  # 导入模板

workbook = xlsxwriter.Workbook('hello.xlsx')  # 创建一个名为 hello.xlsx 赋值给workbook
worksheet = workbook.add_worksheet()  # 创建一个默认工作簿 赋值给worksheet
# 工作簿也支持命名，
# 如：workbook.add_worksheet('hello')

worksheet.write('A1', 'Hello world')  # 使用工作簿在 A1地方 写入Hello world
workbook.close()  # 关闭工作簿