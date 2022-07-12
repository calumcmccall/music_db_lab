import pdb

from models.artist import Artist

import repositories.artist_repository as artist_repository

artist1 = Artist("Elvis")

result = artist_repository.create(artist1)

print(result.__dict__)