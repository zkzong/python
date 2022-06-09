# author: admin
# date: 2022/6/8 21:56
import re

import bs4
import openpyxl
import requests

def open_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.30'}
    res = requests.get(url, headers=headers)
    return res

def find_data(res):
    data = []
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    content = soup.find(id='Cnt-Main-Article-QQ')
    target = content.find_all('p', style='TEXT-INDENT: 2em')

    target =iter(target)
    for each in target:
        if each.text.isnumeric():
            data.append([
                re.search(r'\[(.+)\]', next(target).text).group(1),
                re.search(r'\d.*', next(target).text).group(),
                re.search(r'\d.*', next(target).text).group(),
                re.search(r'\d.*', next(target).text).group()
            ])
    return data

def to_excel(data):
    wb = openpyxl.Workbook()
    wb.guess_types = True
    ws = wb.active
    ws.append(['城市', '平均房价', '平均工资', '房价工资比'])
    for each in data:
        ws.append(each)
    wb.save('2017年中国主要城市房价工资比排行榜.xlsx')

def main():
    url = 'https://news.house.qq.com/a/20170702/003985.htm'
    res = open_url(url)
    data = find_data(res)
    to_excel(data)

    # with open('test.txt', 'w', encoding='utf-8') as file:
    #     file.write(res.text)

if __name__ == '__main__':
    main()