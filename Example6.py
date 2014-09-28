# Saving and restoring JSON data with Text Files

import io, json
import twitter
import urllib2
from oauth_login import oauth_login
from twitter_search import twitter_search
import sys

def save_json(filename, data):
	with io.open(filename,'w',encoding='utf-8') as f:
		f.write(unicode(json.dumps(data,ensure_ascii=False)))

def load_json(filename):
	with io.open(filename,encoding='utf-8') as f:
		return f.read()

print "Example 6:"
q='worldcup'
twitter_api=oauth_login()
results=twitter_search(twitter_api,q,max_result=10)
#print results
save_json('save.json',results)
results=load_json('save.json')


print json.dumps(results,indent=1)
