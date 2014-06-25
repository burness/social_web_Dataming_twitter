import envoy
import os
import sys
def new_db_collection(db_name, coll_name):
	r=envoy.run('mongoimport --db %s --collection %s '%(db_name, coll_name))
	print r.std_out


# test
# new_db_collection('test1','test23')
# new_db_collection('test2','test213')
# an error that can't new the collection named test23 or test213

# no collections!!!!
