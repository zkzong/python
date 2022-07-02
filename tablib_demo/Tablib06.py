import tablib
daniel_tests = [
    ('11/24/09', 'Math 101 Mid-term Exam', 56.),
    ('05/24/10', 'Math 101 Final Exam', 62.)
]

suzie_tests = [
    ('11/24/09', 'Math 101 Mid-term Exam', 56.),
    ('05/24/10', 'Math 101 Final Exam', 62.)
]
tests = tablib.Dataset()
tests.headers = ['Date', 'Test Name', 'Grade']

# Daniel数据测试
tests.append_separator('Daniel的得分')

for test_row in daniel_tests:
   tests.append(test_row)

# Susie数据测试
tests.append_separator('Susie的得分')

for test_row in suzie_tests:
   tests.append(test_row)

# 写入到Eccel表格
with open('grades.xls', 'wb') as f:
    f.write(tests.export('xls'))

