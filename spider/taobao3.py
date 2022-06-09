# author: admin
# date: 2022/6/9 14:12
# 统计淘宝上某一件商品的月销量-解析页面源码
import json
import re


def get_space_end(level):
    return ' ' * level + '-'

def get_space_expand(level):
    return ' ' * level + '+'

def find_keys(targets, level):
    keys = iter(targets)
    for each in keys:
        if type(targets[each]) is not dict:
            print(get_space_end(level) + each)
        else:
            next_level = level + 1
            print(get_space_expand(level) + each)
            find_keys(targets[each], next_level)


def main():
    with open('items.txt', 'r', encoding='utf-8') as file:
        g_page_config = re.search(r'g_page_config=(.*?);\n', file.read())
        page_config_json = json.loads(g_page_config.group(1))
        find_keys(page_config_json)

if __name__ == "__main__":
    main()