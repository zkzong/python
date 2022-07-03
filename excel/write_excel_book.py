import os
import pyexcel as pe

def main(base_dir):
    data = {
        "Sheet 1": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        "Sheet 2": [['X', 'Y', 'Z'], [1, 2, 3], [4, 5, 6]],
        "Sheet 3": [['O', 'P', 'Q'], [3, 2, 1], [4, 3, 2]]
    }
    pe.save_book_as(bookdict=data, dest_file_name="file/third/multiple-sheets1.xls")

if __name__ == '__main__':
    main(os.getcwd())
