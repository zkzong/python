# author: admin
# date: 2022/6/9 14:12
# 统计淘宝上某一件商品的月销量-解析页面源码
import re


def main():
    with open('items.txt', 'r', encoding='utf-8') as file1:
        g_page_config = re.search(r'g_page_config=(.*?);\n', file1.read())
        with open('g_page_config.txt', 'w', encoding='utf-8') as file2:
            file2.write(g_page_config.group(1))

if __name__ == "__main__":
    main()