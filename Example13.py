# Tabulating Frequency Analysis
from prettytable import PrettyTable
from oauth_login import oauth_login
from twitter_search import twitter_search
from get_common_tweet_entities import get_common_tweet_entities

# Get some frequency data
twitter_api=oauth_login()
q='WorldCup'
search_results=twitter_search(twitter_api, q, max_results=100)
common_entities=get_common_tweet_entities(search_results)

# Use PrettyTable to create a nice tabular display
pt=PrettyTable(field_names=['Entity','Count'])
"""Add a row to the table

        Arguments:

        row - row of data, should be a list with as many elements as the table
        has fields"""
[ pt.add_row(kv) for kv in common_entities]
pt.align['Entity'],pt.align['Count']='l','r'
print pt
