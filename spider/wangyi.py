# author: zong
# date: 2022/6/3 19:59

import requests

def get_url(url):
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.30'}
    res = requests.get(url, headers=header)
    return res

def main():
    # https://music.163.com/#/song?id=4466775
    url = input('请输入链接地址：')
    res = get_url(url)
    with open('res.txt', 'w', encoding='utf-8') as f:
        f.write(res.text)

if __name__ == '__main__':
    main()