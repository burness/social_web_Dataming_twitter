import envoy
import os
import sys

# r=envoy.run('mongoimport')
# print r.std_out
# print r.std_err
# data_file=os.path.join(os.getcwd(),'data\enron.mbox.json')
# print data_file

# Run the command just as you would in a terminal to import the data file into MongoDB.
# r=envoy.run('mongoimport --db enron --collection mbox '+ '--file %s'%data_file)
r=envoy.run('mongoimport --db test1 --collection test23 '+ '--file ./data/enron.mbox.json')

print r.std_out
print sys.stderr.write(r.std_err)

# enron.mbox imported to the collection mbox in enron amd it's ok!!!
