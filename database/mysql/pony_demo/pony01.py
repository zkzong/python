import datetime
import pony.orm as pny

database = pny.Database("sqlite",
                        "music.sqlite",
                        create_db=True)
########################################################################
class Artist(database.Entity):
    """
    使用Pony ORM创建表Artist
   """
    name = pny.Required(str)
    albums = pny.Set("Album")
########################################################################
class Album(database.Entity):
    """
    使用Pony ORM创建表Album
    """
    artist = pny.Required(Artist)
    title = pny.Required(str)
    release_date = pny.Required(datetime.date)
    publisher = pny.Required(str)
    media_type = pny.Required(str)

# 打开调试模式
pny.sql_debug(True)
# 映射模型数据库
# 如果它们不存在则创建表
database.generate_mapping(create_tables=True)