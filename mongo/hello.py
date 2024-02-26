from flask import Flask, jsonify, send_from_directory
import json
from mongita import MongitaClientDisk

app = Flask(__name__)


# create a mongita client connection
client = MongitaClientDisk()

# create a movie database
movie_db = client.movie_db

# create a scifi collection
scifi_collection = movie_db.scifi_collection

@app.route("/data/movies/scifi")
def get_data_movies_scifi():
   # with open("","r") as f:
    #    data =json.load(f)
        data = list(scifi_collection.find({}))
        for item in data:
                del item["_id"]
        return jsonify(data)