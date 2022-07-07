import openpyxl

wb = openpyxl.load_workbook("file/third/template.xlsx")
the_list = []

while True:
    info = input('请输入关键字查找：').upper().strip()
    if len(info) == 0:  # 输入的关键字不能为空，否则继续循环
        continue
    count = 0
    for line1 in wb['Sheet3'].values:  # 轮询列表
        if None not in line1:
            ##excel中空行的数据表示None，当这里匹配None时就不会在进行for循环，所以需要匹配非None的数据才能进行下面的for循环。
            for line2 in line1:  # 由于列表中还存在元组，所以需要将元组的内容也轮询一遍
                if info in line2:
                    count += 1  # 统计关键字被匹配了多少次
                    print(line1)  # 匹配关键字后打印元组信息

    else:
        print('匹配"%s"的数量统计：%s个条目被匹配' % (info, count))  # 打印查找的关键字被匹配了多少次
