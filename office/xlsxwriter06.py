import xlsxwriter

workbook = xlsxwriter.Workbook('chart_scatter.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': 1})

# 添加图表将引用的表格中的数据
headings = ['Number', 'Batch 1', 'Batch 2']
data = [
    [2, 3, 4, 5, 6, 7],
    [10, 40, 50, 20, 10, 50],
    [30, 60, 70, 50, 40, 30],
]

worksheet.write_row('A1', headings, bold)
worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])
worksheet.write_column('C2', data[2])

# 创建一个散点图表.
chart1 = workbook.add_chart({'type': 'scatter'})

# 配置第一个系列散点.
chart1.add_series({
    'name': '=Sheet1!$B$1',
    'categories': '=Sheet1!$A$2:$A$7',
    'values': '=Sheet1!$B$2:$B$7',
})

#配置第二个系列散点，注意使用替代语法来定义范围
chart1.add_series({
    'name':       ['Sheet1', 0, 2],
    'categories': ['Sheet1', 1, 0, 6, 0],
    'values':     ['Sheet1', 1, 2, 6, 2],
})

# 添加图表标题和一些轴标签。
chart1.set_title ({'name': 'Results of sample analysis'})
chart1.set_x_axis({'name': 'Test number'})
chart1.set_y_axis({'name': 'Sample length (mm)'})

# 设置excel图表样式。
chart1.set_style(11)

# 将图表插入工作表（带偏移量）。
worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})
workbook.close()