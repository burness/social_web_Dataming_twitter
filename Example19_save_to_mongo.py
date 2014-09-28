from functools import partial
import sys
from sys import maxint
import json

def get_friends_followers_ids_mongo(twitter_api, screen_name=None, user_id=None, friends_limit=maxint,followers_limit=maxint):
	assert(screen_name!=None)!=(user_id!=None),\
	"Must have screen_name or user_id, but not both"

	from make_twitter_request import make_twitter_request
	get_friends_ids=partial(make_twitter_request, twitter_api.friends.ids,count=5000)
	get_followers=partial(make_twitter_request, twitter_api.followers.ids,count=5000)
	if screen_name is not None:
		responese_friends_ids=get_friends_ids(screen_name=screen_name)
		responese_followers_ids=get_followers(screen_name=screen_name)
	else:
		responese_friends_ids=get_friends_ids(user_id=user_id)
		responese_followers_ids=get_followers(user_id=user_id)
	return responese_friends_ids,responese_followers_ids

from oauth_login import oauth_login


twitter_api=oauth_login()
# friends_ids,follower_ids=get_friends_followers_ids(twitter_api,screen_name="SocialWebMining",friends_limit=10,followers_limit=10)

friends_ids,followers_ids=get_friends_followers_ids_mongo(twitter_api,screen_name="SocialWebMining")
print friends_ids
print followers_ids
from save_to_mongo import save_to_mongo

save_to_mongo(friends_ids,"friends_ids","SocialWebMining")
save_to_mongo(followers_ids,"followers_ids","SocialWebMining")
print "save to mongo is ok!!!"

# from new_db_collection import new_db_collection
# #new_db_collection('follower_ids',"SocialWebMining")
# print 'new_db_collection is ok'
# save_to_mongo(followers_ids,"followers_ids","SocialWebMining")
# print "it's ok"