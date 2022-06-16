# author: admin
# date: 2022/6/13 12:17
import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='test', charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL删除记录语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (19)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 向数据库提交
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()
