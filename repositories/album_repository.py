from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album

#CREATE ALBUM

def create(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    print(results)
    id = results[0]['id']
    album.id = id
    return album