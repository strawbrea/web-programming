import json
from mongita import MongitaClientDisk
classic_sci_fi_movies = [...]

client = MongitaClientDisk()

# create a movie database
movie_db = client.movie_db

# create a scifi collection
scifi_collection = movie_db.scifi_collection

# empty the collection
scifi_collection.delete_many({})

# put the movies in the database
scifi_collection.insert_many(classic_sci_fi_movies)

# make sure the movies are there
scifi_collection.count_documents({})