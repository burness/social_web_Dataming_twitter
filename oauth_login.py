import twitter
import urllib2


def oauth_login():
    CONSUMER_KEY='e7KiYQz1koMZOuxNtyxu9pjyK'
    CONSUMER_SECRET='6bHUHyQwPdxQlIOiKSVyFHNAEI2cel6qibaat3wQk2RV0ls0FO'
    OAUTH_TOKEN='969272604-iw8OzM90fFCDHoHGQrBQuMXXd1q2wISXtZKj5THz'
    OAUTH_TOKEN_SECRET='mBkDJe2aq1HWBX1LXRK6Vs0Mz8HvgrOGhccbFItUgUISq'

    auth=twitter.oauth.OAuth(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,
                         CONSUMER_KEY,CONSUMER_SECRET)
    # with proxy_support,first you must set the goagent
    #proxy_support = urllib2.ProxyHandler({'https':'https://127.0.0.1:8087'})
    # with other proxy soft
    proxy_support = urllib2.ProxyHandler({'https':'https://127.0.0.1:8580'})
    opener=urllib2.build_opener(proxy_support,urllib2.HTTPHandler)
    urllib2.install_opener(opener)

    twitter_api=twitter.Twitter(auth=auth)

    return twitter_api


# test the oauth_login function
#twitter_api=oauth_login()
#print twitter_api
