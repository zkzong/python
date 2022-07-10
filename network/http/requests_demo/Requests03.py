import requests
import json

r = requests.post('https://api.github.com/some/endpoint', data=json.dumps({'some': 'data'}))
print(r.json())
response = requests.get("http://httpbin.org/get")
print(type(response.text))
print(response.json())
print(json.loads(response.text))
