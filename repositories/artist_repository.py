from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

#CREATE ARTIST

def create(artist):
    sql = "INSERT INTO artist (name)"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist






#SAVE ARTIST