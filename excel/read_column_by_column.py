import os
import pyexcel as pe

def main(base_dir):
    spreadsheet = pe.get_sheet(file_name=os.path.join(base_dir, "file/example.xlsx"))
    for value in spreadsheet.columns():
        print(value)

if __name__ == '__main__':
    main(os.getcwd())
