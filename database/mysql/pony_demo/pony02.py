import datetime
import pony.orm as pny

from pony01 import Album, Artist


# ----------------------------------------------------------------------
@pny.db_session
def add_data():
    """"""

    new_artist = Artist(name=u"Newsboys")
    bands = [u"MXPX", u"Kutless", u"Thousand Foot Krutch"]
    for band in bands:
        artist = Artist(name=band)

    album = Album(artist=new_artist,
                  title=u"Read All About It",
                  release_date=datetime.date(1988, 12, 1),
                  publisher=u"Refuge",
                  media_type=u"CD")

    albums = [{"artist": new_artist,
               "title": "Hell is for Wimps",
               "release_date": datetime.date(1990, 7, 31),
               "publisher": "Sparrow",
               "media_type": "CD"
               },
              {"artist": new_artist,
               "title": "Love Liberty Disco",
               "release_date": datetime.date(1999, 11, 16),
               "publisher": "Sparrow",
               "media_type": "CD"
               },
              {"artist": new_artist,
               "title": "Thrive",
               "release_date": datetime.date(2002, 3, 26),
               "publisher": "Sparrow",
               "media_type": "CD"}
              ]

    for album in albums:
        a = Album(**album)


if __name__ == "__main__":
    add_data()

    # use db_session as a context manager
    with pny.db_session:
        a = Artist(name="Skillet")