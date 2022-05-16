# author: zong
# date: 2022/5/16 21:28

with open('a.txt', 'r', encoding='utf-8') as f:
    print(f.read())


# 上下文管理器
# 上下文管理器是一个类，它实现了__enter__()和__exit__()方法
class MyContextManager:
    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')

    def show(self):
        # print('show', 1 / 0)
        print('show')

with MyContextManager() as f:
    f.show()

with open('git.png', 'rb') as src_file:
    with open('git2copy.png', 'wb') as target_file:
        target_file.write(src_file.read())