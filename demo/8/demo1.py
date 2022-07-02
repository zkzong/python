scores = (('广州恒大', 72), ('北京国安', 68), ('上海申花', 66), ('江苏苏宁', 53), ('山东鲁能', 51))
for index, item in enumerate(scores):
    print(index + 1, '.', end=' ')
    for score in item:
        print(score, end=' ')
    print()
