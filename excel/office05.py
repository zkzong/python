import pyexcel as p

sheet = p.get_sheet(file_name="file/third/example.csv")
print(sheet)

with open('file/third/tab_example.csv', 'w') as f:
    unused = f.write('I\tam\ttab\tseparated\tcsv\n')  # for passing doctest
    unused = f.write('You\tneed\tdelimiter\tparameter\n')  # unused is added
sheet = p.get_sheet(file_name="file/third/tab_example.csv", delimiter='\t')
print(sheet)
