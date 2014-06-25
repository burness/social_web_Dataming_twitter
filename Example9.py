# Collecting time-series data
import sys
import datetime
import time
import twitter
from functools import partial

def get_time_series_data(api_func, mongo_db_name, mongo_db_coll,
	secs_per_interval=60,max_intervals=15, **mongo_conn_kw):
	# Default setting of 15 intervals and 1 API call per interval ensure
	# that you will not exceed the twitter rate limit
	interval=0
	while True:
		now=str(datetime.datetime.now()).split(".")[0]
		from save_to_mongo import save_to_mongo
		ids=save_to_mongo(api_func(),mongo_db_name,mongo_db_coll+"-"+now)


		print >> sys.stderr,"Write {0} trends".format(len(ids))
		print >> sys.stderr,"Zzz..."
		print >> sys.stderr.flush()

		time.sleep(secs_per_interval)
		interval+=1
		if interval>=15:
			break

from twitter_trends import twitter_trends
from oauth_login import oauth_login
twitter_api = oauth_login()
twitter_world_trends=partial(twitter_trends, twitter_api, 1)
get_time_series_data(twitter_world_trends,'time-series','twitter_trends')
print 'get_time_series_data is ok'