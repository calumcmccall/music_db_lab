from unittest import result
from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository

#CREATE ARTIST
def create(artist):
    sql = "INSERT INTO artists (artist_name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

#DELETE ARTIST
def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

#SELECT ARTIST BY ID
def select(id):
    artist = None

    sql = """
        SELECT * FROM artists
        WHERE id = %s
    """
    values = [id]
    
    results = run_sql(sql, values)
    if results:
        result = results[0]
        artist = Artist(result['artist_name'], result['id'])    
    return artist

#SELECT ALL ARTISTS
def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for row in results:
        artist = Artist(row['artist_name'], row['id'])
        artists.append(artist)
    return artists