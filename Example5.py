# Construction convienient function calls using functools.partial
from functools import partial
import json
import twitter
import urllib2
from oauth_login import oauth_login
from twitter_trends import twitter_trends
from twitter_search import twitter_search
pp=partial(json.dumps,indent=1)

twitter_api = oauth_login()

print "Example5:"
world_trends=twitter_trends(twitter_api,1)
print world_trends
twitter_world_trends=partial(twitter_trends, twitter_api, 1)
print "Twitter_world_trends:%s"%pp(twitter_world_trends())
authenticated_twitter_search=partial(twitter_search,twitter_api)
results=authenticated_twitter_search("iPhone")
print pp(results)

authenticated_iphone_twitter_search=partial(authenticated_twitter_search,"iphone")
results=authenticated_iphone_twitter_search()
print pp(results)
