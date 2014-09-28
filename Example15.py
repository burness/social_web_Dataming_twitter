import re
# Extracting a retweet's attribution by using re
def get_rt_attributions(tweet):
	rt_patterns=re.compile(r"(RT|via)((?:\b\W*@\w+)+)",re.IGNORECASE)
	rt_attributions=[]

	if tweet.has_key('retweeted_status'):
		attribution=tweet['retweeted_status']['user']['screen_name'].lower()
		rt_attributions.append(attribution)



	try:
		rt_attributions+=[mention.strip()
		for mention in rt_patterns.findall(tweet['text'])[0][1].split()]
	except IndexError, e:
		pass
	
	return list(set([rta.strip("@").lower() for rta in rt_attributions]))


from oauth_login import oauth_login
twitter_api=oauth_login()
tweet=twitter_api.statuses.show(_id=214746575765913602)
print tweet['text']
print get_rt_attributions(tweet)
print
tweet=twitter_api.statuses.show(_id=345723917798866944)
print get_rt_attributions(tweet)