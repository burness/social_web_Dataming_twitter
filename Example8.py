# Finding topics of interest by using the filtering capablities it offers
import twitter
import sys

q='WorldCup'
print >> sys.stderr,'Filtering the public time line for track="%s"' %(q,)
from oauth_login import oauth_login
twitter_api = oauth_login()
twitter_stream=twitter.TwitterStream(auth=twitter_api.auth)

stream=twitter_stream.statuses.filter(track=q)
for tweet in stream:
	print tweet['text']

# save to a database in a particular collection
# database_name: stream_results, collection_name: q
from new_db_collection import new_db_collection
new_db_collection('stream_results',q)
print 'new_db_collection is ok'
from save_to_mongo import save_to_mongo
save_to_mongo(tweet,'stream_results',q)
print 'save_to_mongo is ok!!!'


# from mongo to load the data
load_results=load_from_mongo('stream_results',q)
print load_results
print 'load_results is ok!!!'