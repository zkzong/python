import requests

r = requests.get(url='http://www.toppr.net')  # 最基本的GET请求
print(r.status_code)  # 获取返回状态
r = requests.get(url='http://www.toppr.net', params={'wd': 'python'})  # 带参数的GET请求
print(r.url)
print(r.text)  # 打印解码后的返回数据
