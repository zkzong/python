from urllib.parse import urlencode

import httplib2

httplib2.debuglevel = 1

h = httplib2.Http('.cache')

data = {'status': 'Test update from Python 3'}

h.add_credentials('diveintomark', 'MY_SECRET_PASSWORD', 'identi.ca')

resp, content = h.request('https://www.baidu.com',
   'POST',
   urlencode(data),
   headers={'Content-Type': 'application/x-www-form-urlencoded'})
