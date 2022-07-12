import pdb

from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist1 = Artist("Elvis")

result = artist_repository.create(artist1)

print(result.__dict__)

album1 = Album("Best of Elvis", "Country", artist1)
album_repository.create(album1)
