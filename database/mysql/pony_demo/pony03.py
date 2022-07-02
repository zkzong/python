import pony.orm as pny

from pony01 import Artist, Album

with pny.db_session:
    band = Artist.get(name="Newsboys")
    print(band.name)
    for record in band.albums:
        print(record.title)
    # 修改数据
    band_name = Artist.get(name="Kutless")
    band_name.name = "Beach Boys"

result = pny.select(i.name for i in Artist)