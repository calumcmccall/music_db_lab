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

# def delete_all():
#     sql = """
#         DELETE albums, artists
#         FROM albums
#         INNER JOIN artists on albums.artist_id = artists.id
#     """
#     run_sql(sql)

# DELETE T1, T2
# FROM T1
# INNER JOIN T2 ON T1.key = T2.key
# WHERE condition;

#DELETE ALBUM 
def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)