def get_common_tweet_entities(statuses, entity_threshold=3):
	from collections import Counter
	from extract_tweet_entities import extract_tweet_entities
	tweet_entities=[ e 
					for status in statuses
						for entity_type in extract_tweet_entities([status])
							for e in entity_type
					]
	#print tweet_entities
	# compute the repeat times of the each entity 
	c=Counter(tweet_entities).most_common()

	return [(k,v)
			for (k,v) in c
				if v>=entity_threshold
			]