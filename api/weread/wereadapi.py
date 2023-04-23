import argparse
from http.cookies import SimpleCookie

import requests
from requests.cookies import cookiejar_from_dict


def parse_cookie_string(cookie_string):
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    cookies_dict = {}
    cookiejar = None
    for key, morsel in cookie.items():
        cookies_dict[key] = morsel.value
        cookiejar = cookiejar_from_dict(
            cookies_dict, cookiejar=None, overwrite=True
        )
    return cookiejar


# 登录接口："https://i.weread.qq.com/user/notebooks"
url = 'https://i.weread.qq.com/user/notebooks'
weread_cookie = 'wr_fp=2979925371; wr_gid=221641324; wr_vid=5700332; wr_skey=6q9bBBXB; wr_pf=0; wr_rt=web@4Q0pSrAzv~nbQUEkp7f_AL; wr_localvid=73832380656faec738b8893; wr_name=Z; wr_avatar=https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJgdor14prMkAVGPjVZIKW0hfpVhMVNm9cnGb7KJDtwZonlTDIBXoCAuhFXFukOKiascVwsEGzAqEg/132; wr_gender=1'
parser = argparse.ArgumentParser
options = parser.parse_args()
weread_cookie = options.weread_cookie
session = requests.Session()
session.cookies = parse_cookie_string(weread_cookie)
resp = session.get(url)
print(resp)
# 获取书架图书信息（bookid）："https://i.weread.qq.com/shelf/sync?userVid=" + str(userVid) + "&synckey=0&lectureSynckey=0"
# 获取图书信息："https://i.weread.qq.com/book/info?bookId=" + bookId
# 获取图书章节信息："https://i.weread.qq.com/book/chapterInfos?" + "bookIds=" + bookId + "&synckeys=0"
# 获取图书中的标注："https://i.weread.qq.com/book/bookmarklist?bookId=" + bookId
# 获取图书中的个人想法："https://i.weread.qq.com/review/list?bookId=" + bookId + "&listType=11&mine=1&synckey=0&listMode=0"
# 获取图书的热门标注："https://i.weread.qq.com/book/bestbookmarks?bookId=" + bookId