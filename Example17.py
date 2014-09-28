# Resolving User Profile Information
def get_user_profile(twitter_api,screen_names=None, User_ids=None):
	assert(screen_names!=None)!=(User_ids!=None),\
	"Must have screen_names or user_ids, but not both"
	items_to_info={}

	items=screen_names or user_ids
	while len(items)>0:
		# join function: li = ['my','name','is','bob']  ' _'.join(li)  my_name_is_bob
		items_str=','.join([str(item) for item in items[:100]])
		print items_str
		items=items[100:]
		if screen_names:
			from make_twitter_request import make_twitter_request
			response=make_twitter_request(twitter_api.users.lookup, screen_name=items_str)
		else:
			response=make_twitter_request(twitter_api.users.lookup,user_id=items_str)

		for user_info in response:
			if screen_names:
				items_to_info[user_info['screen_name']]=user_info
			else:
				items_to_info[user_infor['id']]=user_info

	return items_to_info
from oauth_login import oauth_login
twitter_api=oauth_login()
print get_user_profile(twitter_api,screen_names=["SocialWebMing","ptwobrussell"])