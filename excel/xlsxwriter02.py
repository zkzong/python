import xlsxwriter
filename = 'file/Expenses01.xlsx'
test_book = xlsxwriter.Workbook(filename)
worksheet = test_book.add_worksheet('what')

expenses = (
    ['Rent', 1000],
    ['Gas',   100],
    ['Food',  300],
    ['Gym',    50],
)

# 定义起始的行列 会在这个基础上 行列各加一 作为初始行列
row = 0
col = 0

for item, cost in expenses:
    worksheet.write(row, col, item)
    worksheet.write(row, col+1, cost)
    row += 1

worksheet.write(row, col, '=sum(B0:B4)')
test_book.close()