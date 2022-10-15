import pprint
import re

import requests

url = 'https://vd6.l.qq.com/proxyhttp'
data = {
    "buid": "vinfoad",
    "vinfoparam": "charge=0&otype=ojson&defnpayver=1&spau=1&spaudio=0&spwm=1&sphls=2&host=v.qq.com&refer=v.qq.com&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200m8u46sg%2Fx004391msci.html&sphttps=1&encryptVer=8.1&cKey=DA28B2A2A4DDFC34494C022C13C04186BF0A81E42F2FE956825DA5F7687D0AC711A15B62E127A665E76F3C19F4C61C0FB11A6E16909D52CF2D14841F3A779C9E7C17F903E184086CBD5D53E16050B83F766BC68C2664310AC4D56F405F1C0F486D3093ACF1B25E9F5588EF1F292DFBF8A95D3C7272BD8335EA3617CEAD50C401CCE1E4248E63871A447F069F00EE4127E2FC5CEF92A243FDA7E61D692455787DB6F7C158708B07006A99451C923826B76530A7EF3296BEFBAED9E34A7CE39EB18A55A9E2BF8001525EEC280AD8D8BDF1A97B715EADAA6F15FC29A03B98BE84D6&clip=4&guid=747f4a5ceb406082&flowid=f332e22e19f70a366cfa57671260dee0&platform=10201&sdtfrom=v1010&appVer=3.5.57&unid=&auth_from=&auth_ext=&vid=x004391msci&defn=&fhdswitch=0&dtype=3&spsrt=2&tm=1659968026&lang_code=0&logintoken=&spvvpay=1&spadseg=3&hevclv=0&spsfrhdr=0&spvideo=0&drm=40",
    "adparam": "pf=in&pf_ex=pc&pu=-1&pt=0&platform=10201&from=0&flowid=f332e22e19f70a366cfa57671260dee0&guid=747f4a5ceb406082&coverid=mzc00200m8u46sg&vid=x004391msci&chid=0&tpid=2&refer=https%3A%2F%2Fv.qq.com%2F&url=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200m8u46sg%2Fx004391msci.html&lt=&opid=&atkn=&appid=&uid=&tkn=&rfid=&v=1.4.119&vptag=www_baidu_com%7C%E7%84%A6%E7%82%B9%E5%9B%BE%3A%E6%A0%87%E9%A2%98%3A1%3A%E7%8E%AB%E7%91%B0%E4%B9%8B%E6%88%98&ad_type=LD%7CKB%7CPVL&live=0&appversion=1.5.4&ty=web&adaptor=1&dtype=1&resp_type=json"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47"
}
response = requests.post(url, json=data, headers=headers)
html_data = response.json()['vinfo']
m3u8_url = re.findall('url(.*?),', html_data)[3].split('"')[2]
# pprint.pprint(html_data)
m3u8_data = requests.get(m3u8_url)
print(m3u8_data)