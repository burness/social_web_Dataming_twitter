# Use a document-oriented database such MongoDB to store the data in a convenient
# JSON format
# First, gooogle the MongoDB, and know how to use it
# Second, we use the twitter api to search key word "WorldCup".
# Finally, insert the data in the Mongo collection "search results"


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


def load_from_mongo(mongo_db, mongo_db_coll, return_cursor=False,criteria=None, projection=None, **mongo_conn_kw):
	client=pymongo.MongoClient(**mongo_conn_kw)
	db=client[mongo_db]
	coll=db[mongo_db_coll]


	if criteria is None:
		criteria={}
	if projection is None:
		cursor=coll.find(criteria)
	else:
		cursor=coll.find(criteria, projection)
	if return_cursor:
		return cursor
	else:
		return [item for item in cursor]

# a sample
q='WorldCup'
twitter_api=oauth_login()
results=twitter_search(twitter_api,q,max_results=10)
# result : data, search_redults :db_name, q: collection_name
# before do it , need to new a db and a collection
from new_db_collection import new_db_collection
new_db_collection('search_results',q)
save_to_mongo(results,'search_results',q)
print 'Save to mongo is ok!!!'
load_from_mongo('search_results',q)
