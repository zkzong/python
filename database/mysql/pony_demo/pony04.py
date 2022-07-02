import pony.orm as pny

from pony01 import Artist

with pny.db_session:
    band = Artist.get(name="MXPX")
    band.delete()