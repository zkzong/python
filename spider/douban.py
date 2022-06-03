# author: zong
# date: 2022/6/3 17:59

# 爬取豆瓣Top250电影排行榜
import requests
import bs4
import re

# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.30'}
# res = requests.get('https://movie.douban.com/top250', headers=header)
# # print(res.text)
# soup = bs4.BeautifulSoup(res.text, 'html.parser')
# targets = soup.find_all("div", class_="hd")
# for each in targets:
#     print(each.a.span.text)

def open_url(url):
    # 使用代理
    # proxies = {'http': '127.0.0.1:1080', 'https': '127.0.0.1:1080'}
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.30'}
    # res = requests.get(url, headers=header, proxies=proxies)
    res = requests.get(url, headers=header)
    return res

def find_movies(res):
    print(res.text)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # 电影名
    movies = []
    targets = soup.find_all("div", class_="hd")
    for each in targets:
        movies.append(each.a.span.text)
    # 评分
    ranks = []
    targets = soup.find_all("span", class_="rating_num")
    for each in targets:
        ranks.append('评分：%s' % each.text)
    # 资料
    messages = []
    targets = soup.find_all("div", class_="bd")
    for each in targets:
        try:
            messages.append(each.p.text.split('\n')[1].strip() + each.p.text.split('\n')[2].strip())
        except:
            continue

    result = []
    length = len(movies)
    for i in range(length):
        result.append(movies[i] + ranks[i] + messages[i] + '\n')
    return result

# 找出一共有多少个页面
def find_depth(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    depth = soup.find("span", class_="next").previous_sibling.previous_sibling.text
    return int(depth)

def main():
    host = 'http://movie.douban.com/top250'
    res = open_url(host)
    depth = find_depth(res)

    result = []
    for i in range(depth):
        url = host + '/?start=' + str(25 * i)
        res = open_url(url)
        result.extend(find_movies(res))

    with open('豆瓣TOP250电影.txt', 'w', encoding='utf-8') as f:
        for each in result:
            f.write(each)

if __name__ == '__main__':
    main()