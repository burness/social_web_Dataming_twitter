import json
import pymongo
from oauth_login import oauth_login
from twitter_search import twitter_search

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
