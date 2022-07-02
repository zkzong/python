import tablib
students = tablib.Dataset()
students.headers = ['first', 'last']
students.rpush(['Kenneth', 'Reitz'], tags=['male', 'technical'])
students.rpush(['Bessie', 'Monke'], tags=['female', 'creative'])
print(students.filter(['male']).yaml)