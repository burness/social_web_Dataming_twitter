def twitter_trends(twitter_api, woe_id):
    return twitter_api.trends.place(_id=woe_id)