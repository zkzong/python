import pyexcel as p
sheet = p.get_sheet(file_name="file/example.csv")
print(sheet)

with open('file/tab_example.csv', 'w') as f:
     unused = f.write('I\tam\ttab\tseparated\tcsv\n') # for passing doctest
     unused = f.write('You\tneed\tdelimiter\tparameter\n') # unused is added
sheet = p.get_sheet(file_name="file/tab_example.csv", delimiter='\t')
print(sheet)