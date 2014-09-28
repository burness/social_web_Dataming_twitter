from functools import partial
import sys
from sys import maxint
import json

def get_friends_followers_ids(twitter_api, screen_name=None, user_id=None, friends_limit=maxint,followers_limit=maxint):
	assert(screen_name!=None)!=(user_id!=None),\
	"Must have screen_name or user_id, but not both"

	from make_twitter_request import make_twitter_request
	get_friends_ids=partial(make_twitter_request, twitter_api.friends.ids,count=5000)
	get_follwers_ids=partial(make_twitter_request, twitter_api.followers.ids,count=5000)
	friends_ids,follower_ids=[],[]

	for twitter_api_func, limit, ids, label in [[get_friends_ids, friends_limit, friends_ids,"friends"],[get_follwers_ids, followers_limit, follower_ids,"followers"]]:

		if limit==0:
			continue
		cursor=-1
		while cursor !=0:
			if screen_name:
				response=twitter_api_func(screen_name=screen_name,cursor=cursor)
				#print type(response)

			else:
				response=twitter_api_func(user_id=user_id, cursor=cursor)
				#print type(response)
			if response is not None:
				ids+= response['ids']
				cursor=response['next_cursor']
			print >> sys.stderr,'Fetch {0} total {1} ids for {2}'.format(len(ids),label,(user_id or screen_name))
			if len(ids)>=limit or response is None:
				break

	return friends_ids[:friends_limit],follower_ids[:followers_limit]

from oauth_login import oauth_login


twitter_api=oauth_login()
# friends_ids,follower_ids=get_friends_followers_ids(twitter_api,screen_name="SocialWebMining",friends_limit=10,followers_limit=10)

friends_ids,followers_ids=get_friends_followers_ids(twitter_api,screen_name="SocialWebMining")
#print friends_ids
#print follower_ids
from save_to_mongo import save_to_mongo

friends_ids=json.dumps(friends_ids, indent=1)
followers_ids=json.dumps(followers_ids,indent=1)
print followers_ids
# if friends_ids:
# 	print "No friends"
# else:
# 	save_to_mongo(friends_ids,"friends_ids","SocialWebMining")
# if follower_ids:
# 	print "No followers"
# else:
# 	save_to_mongo(follower_ids,"followers_ids","SocialWebMining")
# print "it's ok"
# from new_db_collection import new_db_collection
# #new_db_collection('follower_ids',"SocialWebMining")
# print 'new_db_collection is ok'
# save_to_mongo(followers_ids,"followers_ids","SocialWebMining")
# print "it's ok"