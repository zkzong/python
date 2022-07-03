import os
import pyexcel as pe

def main(base_dir):
    book = pe.get_book(file_name=os.path.join(base_dir, "file/third/multiple-sheets-example.xls"))

    # 默认的迭代器为Boo实例
    for sheet in book:
        # 每张表都有名字
        print("sheet: %s" % sheet.name)
        # 一旦您拥有了一个表实例，
        #您就可以将其视为一个读取器实例。我们可以按照您想要的方式迭代它的成员。
        for row in sheet:
            print(row)

if __name__ == '__main__':
    main(os.getcwd())
