# AppId: iP4fiy7dxPeqLNtQNvVun8
# AppSecret: 9e4cc8149ee45833121f55946bfa176972ab60d635964c1e4b708965fd2145e3
import requests

base_url = 'https://openapi.wolai.com/v1'

# 创建Token
url = '/token'

req = {
    "appId": "iP4fiy7dxPeqLNtQNvVun8",
    "appSecret": "9e4cc8149ee45833121f55946bfa176972ab60d635964c1e4b708965fd2145e3"
}
# resp = requests.post(url=base_url + url, json=req, verify=False)
# print(resp)
# print(resp.text)

token = '488498d6b36dc168501311dbbf08e166be6a2791a5198fbb4bce0e02daec8302'

headers = {
    "Authorization": token
}

# 创建块
# parent_id可以是页面id或块id
url = '/blocks'
req = {
    "parent_id": "2A6jreZuG6GPvdG1aNQRv",
    "blocks": [
        {
            "type": "text",
            "content": "Hello ",
            "text_alignment": "center"
        },
        {
            "type": "heading",
            "level": 1,
            "content": {
                "title": "World!",
                "front_color": "red"
            },
            "text_alignment": "center"
        }
    ]
}
# resp = requests.post(url=base_url + url, headers=headers, json=req, verify=False)
# print(resp)
# print(resp.text)

# 获取块信息
url = '/blocks/2A6jreZuG6GPvdG1aNQRv'
resp = requests.get(url=base_url + url, headers=headers, verify=False)
print(resp)
print(resp.text)