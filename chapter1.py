import twitter
import urllib2

CONSUMER_KEY='e7KiYQz1koMZOuxNtyxu9pjyK'
CONSUMER_SECRET='6bHUHyQwPdxQlIOiKSVyFHNAEI2cel6qibaat3wQk2RV0ls0FO'
OAUTH_TOKEN='969272604-iw8OzM90fFCDHoHGQrBQuMXXd1q2wISXtZKj5THz'
OAUTH_TOKEN_SECRET='mBkDJe2aq1HWBX1LXRK6Vs0Mz8HvgrOGhccbFItUgUISq'


auth=twitter.oauth.OAuth(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,
                         CONSUMER_KEY,CONSUMER_SECRET)

# with proxy_support,first you must set the goagent
proxy_support = urllib2.ProxyHandler({'https':'https://127.0.0.1:8087'})
opener=urllib2.build_opener(proxy_support,urllib2.HTTPHandler)
urllib2.install_opener(opener)
twitter_api=twitter.Twitter(domain='api.twitter.com',
                            api_version='1.1',
                            auth=auth
                            )

WORLD_WOE_ID=1
US_WOE_ID=23424977
world_trends=twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends=twitter_api.trends.place(_id=US_WOE_ID)
print [trend['name'] for trend in world_trends[0]['trends']]
print [trend['name'] for trend in us_trends[0]['trends']]


# Displaying API reponses as pretty-printed JSON
import json
print json.dumps(world_trends,indent=1)
print
print json.dumps(us_trends,indent=1)



# Computing the intersection of two sets of trends
world_trends_set=set([trend['name']
                      for trend in world_trends[0]['trends']])
us_trends_set=set([trend['name']
                   for trend in us_trends[0]['trends']])

common_trends=world_trends_set.intersection(us_trends_set)
print 'common_trends:'
print 
print common_trends


# Collecting search results

# Set a Variable to a trending topic,
# or anything else for that matter. The example query below
# was a trending topic when this content was being developed
# and is used throughout the remainder of this chapter

q='#SexyFoods'
count=100
search_results=twitter_api.search.tweets(q=q,count=count)
statuses=search_results['statuses']
for _ in range(5):
    print "Length of statuses",len(statuses)
    try:
        next_results=search_results['search_metadata']['next_results']
    except KeyError,e:
        break
    # handle the data, first split the kv with '&', then split with '=' to
    # get the information like max_id,q,count,include_entities,result_type.
    kwargs=dict([kv.split('=') for kv in next_results[1:].split("&")])
    # 传递任意个有名字的参数，使用dict访问，使用上一条查询结果的next_result的信息来作为查询参数
    # 个人理解有点类似于指针，用于指定下一个内容
    search_results=twitter_api.search.tweets(**kwargs)
    statuses+=search_results['statuses']
print type(statuses)
#print statuses
print json.dumps(statuses[0],indent=1)


# Extracting text, screen_name, and hashtags from tweet
status_texts=[status['text']
              for status in statuses]
screen_names=[user_mention['screen_name']
              for status in statuses
                  for user_mention in status['entities']['user_mentions']]
hashtags=[hashtag['text']
          for status in statuses
              for hashtag in status['entities']['hashtags']]
# Compute a collection of all words from all tweets
words=[w
       for t in status_texts
           for w in t.split()]
# Explore the first 5 items for each...
print json.dumps(status_texts[0:5],indent=1)
print json.dumps(screen_names[0:5],indent=1)
print json.dumps(hashtags[0:5],indent=1)
print json.dumps(words[0:5],indent=1)



# creating a basic frequency distribution from the words in tweets
from collections import Counter
for item in [words, screen_names, hashtags]:
    c=Counter(item)
    print c.most_common()[:10]# top 10
    print



# Using prettytable to display tuples in a nice tabular format
from prettytable import PrettyTable
# loop in order to print 3 table
for label, data in(('Word',words),
                   ('Screen Name',screen_names),
                   ('Hashtag',hashtags)):
    pt=PrettyTable(field_names=[label,'Count'])
    c=Counter(data)
    [pt.add_row(kv) for kv in c.most_common()[:10]]
    pt.align[label],pt.align['Count']='l','r'# Set column alignment
    print pt


# Computing the Lexical Diversity of Tweets
# A function for computing lexical diversity
def lexical_diversity(tokens):
    # set: no repetition
    return 1.0*len(set(tokens))/len(tokens)

# A function for computing the average number of words per tweet
def average_words(statuses):
    total_words=sum([len(s.split()) for s in statuses])
    return 1.0*total_words/len(statuses)

print lexical_diversity(words)
print lexical_diversity(screen_names)
print lexical_diversity(hashtags)
print average_words(status_texts)

# Finding the most popular retweets
retweets=[
    # Store out a tuple of these three values
    # retweet count:转发次数,retweeted_status：转发节点，包括user信息，user中包括screen_name(昵称)
    (status['retweet_count'],
     status['retweeted_status']['user']['screen_name'],
     status['text'])
    
     for status in statuses
     if status.has_key('retweeted_status')# 表示有被转发过
     ]
pt=PrettyTable(field_names=['Count','Screen_Name','Text'])
[pt.add_row(row) for row in sorted(retweets,reverse=True)[:5]]
pt.max_width['Text']=50
pt.align='l'
print pt


# Get the original tweet id for a tweet from its retweeted_status node
# and insert it here in place of the sample value that is provided from
# the text of the book
_retweets = twitter_api.statuses.retweets(id=474726398582468609)
print [r['user']['screen_name'] for r in _retweets]



# Plotting frequencies of words
import matplotlib.pyplot as plt
#print words
word_counts=sorted(Counter(words).values(),reverse=True)
print word_counts
plt.loglog(word_counts)
plt.ylabel("Freq")
plt.xlabel("Word Rank")
#plt.show()

# Generating histograms of words, sreen
for label, data in(('words',words),
                   ('Screen Names',screen_names),
                   ('Hashtags',hashtags)):
    # Build a frequency map for each set of data
    # and plot the values
    c=Counter(data)
    plt.hist(c.values())

    # add a title and y-label
    plt.title(label)
    plt.ylabel("Number of items in bin")
    plt.xlabel("Bins (number of times an item appeared)")
    # ... and display as a new figure
    plt.figure()


# generating a histogram of retweet counts


counts=[count for count ,_, _ in retweets]
    
plt.hist(counts)
plt.title("Retweets")
plt.xlabel('Bins (number of times retweeted)')
plt.ylabel('Number of tweets in bin')
plt.show()

print counts
