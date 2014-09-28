# Finding the Most Popular Tweets in a Collection of Tweets
# Solution: Analyze the retweet_count field of a tweet to determine whether or not
# a tweet was retweeted and if so, how many times
import twitter
import sys

def find_popular_tweets(twitter_api, statuses, retweet_threshold=3):
    return [status
            for status in statuses
            if status['retweet_count'] > retweet_threshold]
# solve the problem"UnicodeEncodeError: 'ascii' codec can't encode character u'\u6211' 
# in position 0: ordinal not in range(128)"
reload(sys)
sys.setdefaultencoding('utf-8')   
q="WorldCup"
from oauth_login import oauth_login
from twitter_search import twitter_search
twitter_api=oauth_login()
search_results=twitter_search(twitter_api, q, max_results=200)
print "search_results is ok!!!"
popular_tweets=find_popular_tweets(twitter_api, search_results)
print "popular_tweets is ok!!!"
print popular_tweets

for tweet in popular_tweets:
	print tweet['text'],tweet['retweet_count']
