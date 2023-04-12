import csv
import threading


def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # 处理每一行CSV数据
            print(row[0])


if __name__ == '__main__':
    filename = 'file/example.csv'
    threads = []
    num_threads = 4  # 设置线程数
    # 创建并启动多个线程
    for i in range(num_threads):
        t = threading.Thread(target=read_csv, args=(filename,))
        threads.append(t)
        t.start()
    # 等待所有线程执行完毕
    for t in threads:
        t.join()
