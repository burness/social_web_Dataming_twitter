import json
import pymongo
from bson import json_util

client=pymongo.MongoClient()
print client
db=client.enron
mbox=db.mbox

print "Numbers of messages in mbox:"
print mbox.count()
print "A message:"
print json.dumps(msg, indent =1, default=json_util.default)