# author: admin
# date: 2022/6/3 17:30

import requests
r = requests.get('https://api.github.com', auth=('user', 'pass'))
print(r.status_code)
print(r.headers['content-type'])

import urllib.request
gh_url = 'https://api.github.com'
req = urllib.request.Request(gh_url)
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, gh_url, 'user', 'pass')
auth_manager = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(auth_manager)
urllib.request.install_opener(opener)
handler = urllib.request.urlopen(req)
print(handler.getcode())
print(handler.headers['content-type'])