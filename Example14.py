# Finding Users who have retweeted a status use the retweeters/ids api
import twitter
import json
from oauth_login import oauth_login


twitter_api=oauth_login()


print """User IDs for retweeters of a tweet by @fperez_org
that was retweeted by @SocialWebMining and that @jyeee then retweeted
from @SocialWebMining's timeline\n"""

# _id is a tweet's id 
print twitter_api.statuses.retweeters.ids(_id=334188056905129984)['ids']
print json.dumps(twitter_api.statuses.show(_id=334188056905129984),indent=1)


print "@SocialWeb's retweet of @fperez_org's tweet\n"
print twitter_api.statuses.retweeters.ids(_id=334188056905129984)['ids']
print json.dumps(twitter_api.statuses.show(_id=334188056905129984),indent=1)


print "@jyeee's retweet of @fperez_org's tweet\n"
print twitter_api.statuses.retweeters.ids(_id=338835939172417537)['ids']
print json.dumps(twitter_api.statuses.show(_id=338835939172417537), indent=1)
