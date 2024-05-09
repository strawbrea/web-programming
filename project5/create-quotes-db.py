# Create a Mongita database with movie information
import json
from mongita import MongitaClientDisk

quotes_data = quotes_data = [
    {"text": "I'm hungry. When's lunch?", "author": "Dorothy", "owner": "Greg", "allow_comments": True},
    {"text": "You threw that ball. You go get it.", "author": "Suzy", "owner": "Dorothy", "allow_comments": False},
]

# create a mongita client connection
client = MongitaClientDisk()

# create a quote database
quotes_db = client.quotes_db

# create a quotes collection
quotes_collection = quotes_db.quotes_collection

# create comments collection
comments_collection = quotes_db.comments
quotes_collection.create_index([("text", "text")])

# empty the collection
quotes_collection.delete_many({})

# put the quotes in the database
quotes_collection.insert_many(quotes_data)

# make sure the quotes are there
print(quotes_collection.count_documents({}))
