import requests
from requests.auth import HTTPBasicAuth
#方法一
r = requests.get('http://120.27.34.24:9001', auth=HTTPBasicAuth('user', '123'))
#方法二<br>r = requests.get('http://120.27.34.24:9001', auth=('user', '123'))
print(r.status_code)