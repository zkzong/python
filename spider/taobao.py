# author: admin
# date: 2022/6/9 14:12
# 统计淘宝上某一件商品的月销量-获取页面源码
import requests


def open_url(keyword):
    payload = {'q':'零基础入门学习Python','sort':'sale-desc'}
    url = 'https://s.taobao.com/search'

    res = requests.get(url, params=payload)
    return res

def main():
    keyword = input('请输入搜索关键词：')
    res = open_url(keyword)
    with open('items.txt', 'w', encoding='utf-8') as file:
        file.write(res.text)

if __name__ == "__main__":
    main()