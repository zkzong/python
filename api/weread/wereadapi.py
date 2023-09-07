import requests

baseurl = "https://i.weread.qq.com"
cookies = {
    "cookies": "tvfe_boss_uuid=ccb7f3a8ed89c5b1; pgv_pvid=5432667300; pac_uid=0_0ce5538f1cb66; iip=0; _clck=3005424110|1|f4r|0; logTrackKey=668cba3c36984e2ca0a403d019893a91; wr_theme=white; wr_vid=5700332; wr_pf=0; wr_localvid=73832380656faec738b8893; wr_name=Z; wr_gender=1; wr_gid=221641324; wr_rt=web%404Q0pSrAzv~nbQUEkp7f_AL; qq_domain_video_guid_verify=747f4a5ceb406082; wr_avatar=https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTJgdor14prMkAVGPjVZIKW0hfpVhMVNm9cnGb7KJDtwZonlTDIBXoCAKgXokx0pvFDJ3GMR6WASug%2F132; wr_skey=KAV7qEch; wr_fp=4258000936"
}

# 获取书架图书信息（bookid）："https://i.weread.qq.com/shelf/sync?userVid=" + str(userVid) + "&synckey=0&lectureSynckey=0"
userVid = '1671972079'
url = "/shelf/sync" + "?userVid=" + userVid + "&synckey=0&lectureSynckey=0"
response = requests.get(url=baseurl + url, cookies=cookies)
# print(response.text)

# 获取图书信息："https://i.weread.qq.com/book/info?bookId=" + bookId
bookId = '3300046920'
url = "/book/info" + "?bookId=" + bookId
response = requests.get(url=baseurl + url, cookies=cookies)
# print(response.text)

# 获取图书章节信息："https://i.weread.qq.com/book/chapterInfos?" + "bookIds=" + bookId + "&synckeys=0"
bookId = '3300046920'
url = "/book/chapterInfos" + "?bookIds=" + bookId + "&synckeys=0"
response = requests.get(url=baseurl + url, cookies=cookies)
# print(response.text)

# 获取用户的Notebook："https://i.weread.qq.com/user/notebooks"
url = "/user/notebooks"
response = requests.get(url=baseurl + url, cookies=cookies)
# print(response.text)

# 获取图书中的标注："https://i.weread.qq.com/book/bookmarklist?bookId=" + bookId
bookId = '3300046920'
url = "/book/bookmarklist" + "?bookId=" + bookId
response = requests.get(url=baseurl + url, cookies=cookies)
# print(response.text)

# 获取图书中的个人想法："https://i.weread.qq.com/review/list?bookId=" + bookId + "&listType=11&mine=1&synckey=0&listMode=0"
bookId = '3300046920'
url = "/review/list" + "?bookId=" + bookId + "&listType=11&mine=1&synckey=0&listMode=0"
response = requests.get(url=baseurl + url, cookies=cookies)
# print(response.text)

# 获取图书的热门标注："https://i.weread.qq.com/book/bestbookmarks?bookId=" + bookId
bookId = '3300046920'
url = "/book/bestbookmarks" + "?bookId=" + bookId
response = requests.get(url=baseurl + url, cookies=cookies)
print(response.text)
