import requests

r = requests.get('http://www.toppr.net')
print(r.text, '\n{}\n'.format('*' * 79), r.encoding)
r.encoding = 'GBK'
print(r.text, '\n{}\n'.format('*' * 79), r.encoding)
