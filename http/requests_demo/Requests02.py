import requests
url = 'http://httpbin.org/get'
data = {
    'name': 'zhangsan',
    'age': '25'
}
response = requests.get(url, params=data)
print(response.url)
print(response.text)