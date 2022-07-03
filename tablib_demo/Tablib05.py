import tablib

'''使用标签过滤数据'''
students = tablib.Dataset()
students.headers = ['first', 'last']
students.rpush(['Kenneth', 'Reitz'], tags=['male', 'technical'])
students.rpush(['Bessie', 'Monke'], tags=['female', 'creative'])
# todo
print(students.filter(['male']).yaml)
