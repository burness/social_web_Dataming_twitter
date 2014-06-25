# Example illustrates how to use the Search API to search tweet for example:
# a key word "worldcup" and navigate
# the cursor that's included in a reponse to fetch more than
# one batch of results

import json
import twitter
import urllib2
from oauth_login import oauth_login


def twitter_search(twitter_api, q, max_results=200, **kw):
    search_results = twitter_api.search.tweets(q=q, count=100, **kw)
    statuses = search_results['statuses']
    # Iterate through batches of results by following the cursor until we reach the
    # desired number of results.
    max_results = min(1000, max_results)
    for _ in range(10):
        try:
            next_results = search_results['search_metadata']['next_results']
        except KeyError, e:
            break
        kwargs = dict([kv.split('=')
                       for kv in next_results[1:].split("&")])
        search_results = twitter_api.search.tweets(**kwargs)
        statuses += search_results['statuses']
        if len(statuses) > max_results:
            break
    return statuses


twitter_api = oauth_login()
q = "worldcup"
results = twitter_search(twitter_api, q, max_results=10)


print json.dumps(results[0], indent=1)
