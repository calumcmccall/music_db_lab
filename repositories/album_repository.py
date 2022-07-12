from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository

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

#SELECT ALBUM BY ID
def select(id):
    album = None

    sql = """
        SELECT * FROM albums
        WHERE id = %s
    """
    values = [id]
    
    results = run_sql(sql, values)
    if results:
        result = results[0]
        artist = artist_repository.select(result['id'])
        album = Album(result['title'], result['genre'], artist, result['id'])
    return album

#SELECT ALL ALBUMS

def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['id'])
        album = Album(row['title'], row['genre'], artist, row['id'])
        albums.append(album)
    return albums