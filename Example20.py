# Analyzing a user's Friends and Followers
def setwise_friends_followers_analysis(screen_name, friends_ids, followers_ids):
	friends_ids,followers_ids=set(friends_ids),set(followers_ids)
	print '{0} is following {1}'.format(screen_name,len(friends_ids))
	print '{0} is being followed by {1}'.format(screen_name, len(followers_ids))
	print '{0} of {1} are folloing {2} back '.format(len(friends_ids.difference(followers_ids)),len(friends_ids),screen_name)
	print '{0} of {1} are not being followed back by {2}'.format(len(followers_ids.difference(friends_ids)),len(followers_ids),screen_name)
	print '{0} has {1} mutual friends'.format(screen_name, len(friends_ids.intersection(followers_ids)))




screen_name="ptwobrussell"
from oauth_login import oauth_login
twitter_api=oauth_login()
from get_friends_followers_ids import get_friends_followers_ids

friends_ids,followers_ids = get_friends_followers_ids(twitter_api,screen_name=screen_name)
setwise_friends_followers_analysis(screen_name,friends_ids,followers_ids)
