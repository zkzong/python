# author: zong
# date: 2022/6/3 19:59

import requests

def get_comments(url):
    # 传给它referer
    # 当然，有时间的话将headers头部填写完整，那样会更好一些
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.30',
              'referer': 'https://music.163.com/'}

    params= 'dcHTvPOve3eoeKyGkWCovA9Wn7h+swcvCxLCE+vJxiQ/BqsRCvDgiB+PHgvHLMe/0l461R0pKU8TZ2/fNrgs5kh/iPfy1s9zA6NybTzDOoS6wzFe9Iqn7T2ED85V6vF+NNNUB/5CQTl+1ycBTWZtJwZiFsqB3f20W7qYaumE0C6oqGrh3cuzSgfuFwh69nuW7d8p5NO5fuEy0sTIVlr8Mzi7K05gvSwfzxGrIbvOEWoli0n1Qh+aWBstMmuiu+wd/v2wgYutwGjYaHSmzhhGig=='
    encSecKey = 'b38136c5495ca86e6b08379378b30c967b50616bf2b382aa3bb880d4adf94e1439c418d9945e46054a5240e521815abde6b1fc6dbbfd7b1f00bb5c25dd0e58ef922d7a215b2962b0879140e2b33d653c6903ed2cf89824037624f7fe3b4425760f5074343756f9e35aefeb90b3e7a1c7dfc1763bc32dfa09a9acbb9ea4a8cf96'
    data = {'params': params, 'encSecKey': encSecKey}

    name_id = url.split('=')[1]
    target_url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token='.format(name_id)
    res = requests.post(target_url, headers=header, data=data)
    return res

def main():
    # https://music.163.com/#/song?id=4466775
    url = input('请输入链接地址：')
    res = get_comments(url)
    with open('data.txt', 'w', encoding='utf-8') as f:
        f.write(res.text)

if __name__ == '__main__':
    main()