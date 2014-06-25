#-*- coding: UTF-8 -*-

# 这个代码我想扩充，然后分析世界比较出名的几个大城市的trend，然后绘成类似于复杂的网络图
# 1，首先收集比较大的城市列表，然后从Yahoo上搜索相应地woe_id
# 2，使用twitter的api搜索出每个城市的trends
# 3，利用networkX构建复杂的网络，然后汇出相应的网络图


import json
import twitter
import urllib2
from oauth_login import oauth_login


def twitter_trends(twitter_api, woe_id):
    return twitter_api.trends.place(_id=woe_id)


twitter_api = oauth_login()
# print "我是段石石"

# 20 top cities
# UnLuckily Beijing and Shanghai has no pages in twitter
cities_woeid = {
    'New York': 2459115,
    'London': 44418,
    'Paris': 615702,
    'Tokyo': 1118370,
    #'Hong Kong': 24865698,
    'Los Angeles': 2442047,
    'Chicago': 2379574,
    #'Beijing':2151330,
    'Singapore': 23424948,
    #'Washington, D.C.': 2514815,
    #'Brussels':968019,
    'Seoul': 1132599,
    'Toronto': 4118,
    'Sydney': 1105779,
    'Madrid': 766273,
    'Vienna': 551801,
    'Moscow': 2122265,
    #'Shanghai':2151849,
    'Berlin': 638242,
    'Buenos Aires': 468739
}
cities_trend = {}
for (k, v) in cities_woeid.items():
    print "City: %s, woe_id: %s" % (k, v)
    woe_id = v
    trends = twitter_trends(twitter_api, woe_id)
    print "The trend name in %s :" % k
    trend_names = [trend['name'] for trend in trends[0]['trends']]
    #print [trend_name.decode('utf-8').encode('GB18030') for trend_name in trend_names]
    print trend_names
    # store in a dict
    cities_trend[k] = trend_names

print cities_trend
f = open('trend_name.txt', 'w')
json.dump(cities_trend,f)
f.close()




# SY_WOE_ID=1105779
# SY_trends=twitter_trends(twitter_api,SY_WOE_ID)
# print SY_trends
# print SY_trends['trends']['name']
# print the name of the trend
# print "The trend name in Sydney:"
# print [trend['name'] for trend in SY_trends[0]['trends']]
# print json.dumps(SY_trends,indent=1)


# US_WOE_ID=23424977
# us_trends=twitter_trends(twitter_api,US_WOE_ID)
# print "The trend name in USA:"
# print [trend['name'] for trend in us_trends[0]['trends']]
# print json.dumps(us_trends,indent=1)
