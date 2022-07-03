import os
import pyexcel as pe
def main(base_dir):
    # 读取的文件"example.xlsm"
    spreadsheet = pe.get_sheet(file_name=os.path.join(base_dir, "file/third/example.csv"))

    # 遍历每一行
    for r in spreadsheet.row_range():
        # 遍历每一列
        for c in spreadsheet.column_range():
            print(spreadsheet.cell_value(r, c))

if __name__ == '__main__':
    main(os.getcwd())
