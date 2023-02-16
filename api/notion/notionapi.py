import requests

base_url = 'https://api.notion.com/v1'
token = 'secret_36REZ6tYNixmAVcndf3toygapV99NTtfzbDMjsYUHAJ'

# Retrieve a page
# url = '/pages/api-b151b883e2234e139edebb74f1d4fc4e'
# headers = {
#     "accept": "application/json",
#     "Notion-Version": "2022-06-28",
#     "Authorization": "Bearer " + token
# }
# print(base_url + url)
# response = requests.get(url=base_url + url, headers=headers, verify=False)
# print(response.text)

# Create a page
# url = '/pages'
# headers = {
#     "accept": "application/json",
#     "Notion-Version": "2022-06-28",
#     "content-type": "application/json",
#     "Authorization": "Bearer " + token
# }
# response = requests.post(url=base_url + url, headers=headers)
# print(response.text)

# Retrieve a block
url = '/blocks/309cc3400de34fcbba185c461080d791'
headers = {
    "accept": "application/json",
    "Notion-Version": "2022-06-28",
    "Authorization": "Bearer " + token
}
response = requests.post(url=base_url + url, headers=headers, verify=False)
print(response.text)
