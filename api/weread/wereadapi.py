import requests

baseurl = "https://i.weread.qq.com"
cookies = "pgv_pvid=2377353160; pac_uid=0_28d4b3c0c6fed; tvfe_boss_uuid=f4d1843b2ccedcd8; wr_theme=white; qq_domain_video_guid_verify=968dc7ecd47ac090; wr_gid=214509499; wr_vid=5700332; wr_pf=0; wr_rt=web%40lnosaZM1gtQNQEAl~u3_AL; wr_localvid=73832380656faec738b8893; wr_name=Z; wr_avatar=https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTJgdor14prMkAVGPjVZIKW0hfpVhMVNm9cnGb7KJDtwZonlTDIBXoCAKgXokx0pvFDJ3GMR6WASug%2F132; wr_gender=1; _clck=3005424110|1|fel|0; wr_fp=1800734459; wr_skey=MKxcGShc"

# 获取书架图书信息（bookid）："https://i.weread.qq.com/shelf/sync?userVid=" + str(userVid) + "&synckey=0&lectureSynckey=0"
userVid = 1671972079
url = "/shelf/sync" + "?userVid=" + str(userVid) + "&synckey=0&lectureSynckey=0"
response = requests.get(url=baseurl + url, headers=cookies)
print(response)
# 获取图书信息："https://i.weread.qq.com/book/info?bookId=" + bookId
# 获取图书章节信息："https://i.weread.qq.com/book/chapterInfos?" + "bookIds=" + bookId + "&synckeys=0"
# 获取用户的Notebook："https://i.weread.qq.com/user/notebooks"
# 获取图书中的标注："https://i.weread.qq.com/book/bookmarklist?bookId=" + bookId
# 获取图书中的个人想法："https://i.weread.qq.com/review/list?bookId=" + bookId + "&listType=11&mine=1&synckey=0&listMode=0"
# 获取图书的热门标注："https://i.weread.qq.com/book/bestbookmarks?bookId=" + bookId
