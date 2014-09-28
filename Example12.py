# Finding the most popular tweet entities in a collection of tweets
import twitter
from collections import Counter
import sys
from extract_tweet_entities import extract_tweet_entities
def get_common_tweet_entities(statuses, entity_threshold=3):
	tweet_entities=[ e 
					for status in statuses
						for entity_type in extract_tweet_entities([status])
							for e in entity_type
					]
	print tweet_entities
	# compute the repeat times of the each entity 
	c=Counter(tweet_entities).most_common()

	return [(k,v)
			for (k,v) in c
				if v>=entity_threshold
			]



# Sample usage
reload(sys)
sys.setdefaultencoding('utf-8')   
q="WorldCup"
from oauth_login import oauth_login
from twitter_search import twitter_search

twitter_api=oauth_login()
search_results=twitter_search(twitter_api, q, max_results=20)
print "Search results is ok!!!"
common_entities=get_common_tweet_entities(search_results)

print "Most common tweet entities"
print common_entities