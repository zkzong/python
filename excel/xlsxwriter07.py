import xlsxwriter

#新建一个excel文件，起名为expense01.xlsx
workbook = xlsxwriter.Workbook("123.xlsx")
#添加一个Sheet页，不添写名字，默认为Sheet1
worksheet = workbook.add_worksheet()
#准备数据
headings=["姓名","数学","语文"]
data=[["C罗张",78,60],["糖人李",98,89],["梅西徐",88,100]]
#样式
head_style = workbook.add_format({"bold":True,"bg_color":"yellow","align":"center","font":13})
#写数据
worksheet.write_row("A1",headings,head_style)
for i in range(0,len(data)):
    worksheet.write_row("A{}".format(i+2),data[i])
#添加柱状图
chart1 = workbook.add_chart({"type":"column"})
chart1.add_series({
    "name":"=Sheet1!$B$1",#图例项
    "categories":"=Sheet1!$A$2:$A$4",#X轴 Item名称
    "values":"=Sheet1!$B$2:$B$4"#X轴Item值
})
chart1.add_series({
    "name":"=Sheet1!$C$1",
    "categories":"=Sheet1!$A$2:$A$4",
    "values":"=Sheet1!$C$2:$C$4"
})
#添加柱状图标题
chart1.set_title({"name":"柱状图"})
#Y轴名称
chart1.set_y_axis({"name":"分数"})
#X轴名称
chart1.set_x_axis({"name":"人名"})
#图表样式
chart1.set_style(11)

#添加柱状图叠图子类型
chart2 = workbook.add_chart({"type":"column","subtype":"stacked"})
chart2.add_series({
    "name":"=Sheet1!$B$1",
    "categories":"=Sheet1!$A$2:$a$4",
    "values":"=Sheet1!$B$2:$B$4"
})
chart2.add_series({
    "name":"=Sheet1!$C$1",
    "categories":"=Sheet1!$A$2:$a$4",
    "values":"=Sheet1!$C$2:$C$4"
})
chart2.set_title({"name":"叠图子类型"})
chart2.set_x_axis({"name":"姓名"})
chart2.set_y_axis({"name":"成绩"})
chart2.set_style(12)

#添加饼图
chart3 = workbook.add_chart({"type":"pie"})
chart3.add_series({
    #"name":"饼形图",
    "categories":"=Sheet1!$A$2:$A$4",
    "values":"=Sheet1!$B$2:$B$4",
    #定义各饼块的颜色
     "points":[
         {"fill":{"color":"yellow"}},
         {"fill":{"color":"blue"}},
         {"fill":{"color":"red"}}
    ]
})
chart3.set_title({"name":"饼图成绩单"})
chart3.set_style(3)


#插入图表
worksheet.insert_chart("B7",chart1)
worksheet.insert_chart("B25",chart2)
worksheet.insert_chart("J2",chart3)

#关闭EXCEL文件
workbook.close()