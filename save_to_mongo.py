import json
import pymongo
from oauth_login import oauth_login
from twitter_search import twitter_search


def save_to_mongo(data, mongo_db, mongo_db_coll, **mongo_conn_kw):
    # Connects to the MongoDB server running on
    # localhost:27017 by default

    client = pymongo.MongoClient(**mongo_conn_kw)
    # Get a reference to a particular database

    db = client[mongo_db]

    coll = db[mongo_db_coll]

    return coll.insert(data)