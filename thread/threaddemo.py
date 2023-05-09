# author: admin
# date: 2023/4/29 15:10
import threading


def my_func(a, b):
    do_craw(a, b)

def do_craw(a, b):
    return a + b

t = threading.Thread(target=my_func, args=(100, 2000))

t.start()

t.join()