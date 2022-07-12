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

# album_repository.delete_all()
# artist_repository.delete_all()

find_elvis_album = album_repository.select(14)
print(find_elvis_album.__dict__)

find_elvis_artist = artist_repository.select(24)
print(find_elvis_artist.__dict__)