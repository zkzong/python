import grequests
urls = [
    'http://www.heroku.com',
    'http://python-tablib.org',
    'http://httpbin.org',
    'http://python-requests.org',
    'http://fakedomain/',
    'http://kennethreitz.com'
]
#创建一组未发送请求
rs = (grequests.get(u) for u in urls)
#同时发送这组请求
print(grequests.map(rs))