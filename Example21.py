# Harvesting a User's Tweets
def harvest_user_timeline(twitter_api, screen_name=None,user_id=None, max_results=1000):
	assert(screen_name!=None)!=(user_id!=None),\
	"must have screen_name or user_id, but not both"
	kw={
	'count':200,
	'trim_user':'true',
	'include_rts':'true',
	'since_id':1
	}
	if screen_name:
		kw['screen_name']=screen_name
	else:
		kw['user_id']=user_id
	max_pages=16
	max_results=[]
	from make_twitter_request import make_twitter_request
	tweet=make_twitter_request(twitter_api.statuses.user_timeline,**kw)
	if tweets is None:
		tweets=[]
	results+=tweets
	print >> sys.stderr,'Fetched %i tweets' %len(tweets)
	page_num=1
	if max_results==kw['count']:
		page_num=max_pages
	while page_num <max_pages and len(tweets)>0 and len(results)< max_results:
		kw['max_id']=min([tweet['id'] for tweet in tweets])-1
		tweets=make_twitter_request(twitter_api.statuses.user_timeline,**kw)
		results+=tweets
		print >> sys.stderr, 'Fetched %i tweets' %(len(tweets),)
		page_num+=1
	print >> sys.stderr,'Done fetching tweets'
	return results[:max_results]

