import os
import pyexcel as pe
import json

def main(base_dir):
    sheet = pe.get_sheet(file_name=os.path.join(base_dir, "file/example_series.xls"),
                         name_columns_by_row=0)
    print(json.dumps(sheet.to_dict()))
    # 获取列标题
    print(sheet.colnames)
    # 在一维数组中获取内容
    data = list(sheet.enumerate())
    print(data)
    # 逆序获取一维数组中的内容
    data = list(sheet.reverse())
    print(data)

    # 在一维数组中获取内容，但垂直地迭代它
    data = list(sheet.vertical())
    print(data)
    # 获取一维数组中的内容，遍历垂直revserse顺序
    data = list(sheet.rvertical())
    print(data)

    # 获取二维数组数据
    data = list(sheet.rows())
    print(data)

    # 以相反的顺序获取二维数组
    data = list(sheet.rrows())
    print(data)

    # 获取二维数组，堆栈列
    data = list(sheet.columns())
    print(data)

    # 获取一个二维数组，以相反的顺序叠列。
    data = list(sheet.rcolumns())
    print(data)

    # 可以把结果写入一个文件中
    sheet.save_as("example_series.xls")

if __name__ == '__main__':
    main(os.getcwd())
