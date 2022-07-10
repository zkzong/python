import grequests
import requests
import cProfile

urls = [
    'http://www.xiachufang.com/downloads/baidu_pip/2016030101.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030102.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030103.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030104.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030105.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030106.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030107.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030108.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030109.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030110.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030111.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030112.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030113.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030114.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030115.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030116.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030117.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030118.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030119.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030120.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030121.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030122.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030123.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030200.json',
]
def haha(urls):
    rs = (grequests.get(u) for u in urls)
    return grequests.map(rs)

cProfile.run("haha(urls)")

def hehe(urls):
    hehe = [requests.get(i) for i in urls]
    return hehe

cProfile.run("haha(urls)")