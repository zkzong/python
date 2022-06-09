# author: admin
# date: 2022/6/9 21:53

# 找出B站最受欢迎的编程课程
import bs4
import requests

res = requests.get('https://search.bilibili.com/all?keyword=%E7%BC%96%E7%A8%8B&from_source=webtop_search&spm_id_from=333.1007')
# print(res.text)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
titles = soup.find_all('li', class_='video-matrix')
for each in titles:
    print(each.a['title'])