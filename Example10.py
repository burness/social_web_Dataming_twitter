# Extracting Tweet Entities
def extract_tweet_entities(statuses):
    if len(statuses) == 0:
        return [], [], [], []
    screen_names = [user_mention['screen_name']
                    for status in statuses
                    for user_mention in status['entities']['user_mentions']]
    hashtags = [hashtag['text']
                for status in statuses
                for hashtag in status['entities']['hashtags']]
    urls = [url['expanded_url']
            for status in statuses
            for url in status['entities']['urls']]
    symbols = [symbol['text']
               for status in statuses
               for symbol in status['entities']['symbols']]
    if status['entities'].has_key('media'):
        media = [media['url']
                 for status in statuses
                 for media in status['entities']['media']]
    else:
        media = []

    return screen_names, hashtags, urls, media, symbols

from oauth_login import oauth_login
from twitter_search import twitter_search
import json
twitter_api = oauth_login()
q = 'WorldCup'
statuses = twitter_search(twitter_api, q, max_results=10)
print "statuses:%s" % statuses
screen_names, hashtags, urls, media, symbols = extract_tweet_entities(statuses)
print "extract_tweet_entities is ok!!!"

# Explore the first five items for each...
print json.dumps(screen_names[0:5], indent=1)
print json.dumps(hashtags[0:5], indent=1)
print json.dumps(urls[0:5], indent=1)
print json.dumps(media[0:5], indent=1)
print json.dumps(symbols[0:5], indent=1)
