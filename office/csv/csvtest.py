import csv

a = open('file/test.csv', encoding='utf-8')
reader = csv.reader(a)
rows = [row for row in reader]
for row in rows:
    print(row[0])
