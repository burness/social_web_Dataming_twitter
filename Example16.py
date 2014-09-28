# Making Robust Twitter Request
# Encounter unexpected HTTP Errors that range from exceeding your rate limits
# to the infamous "fail whale"

# Write a function that serves as a general-purpose API wrapper and provides abstracted
# logic for handling various HTTP error codes in meaningful ways

import sys
import time
from urllib2 import URLError
from httplib import BadStatusLine
import json
import twitter


def make_twitter_request(twitter_api_func, max_errors=10, *args, **kw):

    def handle_twitter_http_error(e, wait_period=2, sleep_when_rate_limited=True):

        if wait_period > 3600:
            print >> sys.stderr
            raise e

        if e.e.code == 401:
            print >> sys.stderr, 'Encountered 401 error (Not Authorized)'
            return None

        elif e.e.code == 404:
            print >> sys.stderr, 'Encountered 404 Error (Not Found)'
            return None

        elif e.e.code == 429:
            print >> sys.stderr, 'Encountered 429 Error (Rate Limit Exceeded)'
            if sleep_when_rate_limited:
                print >> sys.stderr, "Retring in 15 minutes...ZzZ..."
                sys.stderr.flush()
                time.sleep(60 * 15 + 5)
                print >> sys.stderr, '...ZzZ... Awake now and tring again.'
                return 2
            else:
                raise e
        elif e.e.code in (500, 502, 503, 504):
                print >> sys.stderr, 'Encountered %i Error. Retring in %i seconds' % (
                    e.e.code, wait_period)
                time.sleep(wait_period)
                wait_period *= 1.5
                return wait_period
        else:
            raise e

    wait_period = 2
    error_count = 0

    while True:
        try:
            print kw
            print args
            return twitter_api_func(*args,**kw)
        except twitter.api.TwitterHTTPError,e:
            error_count=0
            wait_period=handle_twitter_http_error(e,wait_period)
            if wait_period is None:
                return 
        except URLError,e:
            error_count+=1
            print >> sys.stderr,"URLError encountered. Continuing"
            if error_count>max_errors:
                print >> sys.stderr,"Too many consecutive errors...bailing out"
                raise
        except BadStatusLine,e:
            error_count+=1
            print >> sys.stderr,"BadStatusLine encountered. Continuing"
            if error_count>max_errors:
                print >> sys.stderr,"Too many consecutive errors... bailing out"
                raise



from oauth_login import oauth_login
twitter_api=oauth_login()
# response=twitter_api.users.lookup(screen_name='SocialWebMining')
# print twitter_api.users.lookup(screen_name='SocialWebMining')
response=make_twitter_request(twitter_api.users.lookup,screen_name="SocialWebMining")
print json.dumps(response,indent=1)
