#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymongo
import time

conn = pymongo.MongoClient(host="127.0.0.1", port=27017)
print(conn.list_database_names())
#db.authenticate('username', 'password')
db=conn.get_database("test")
print(db.collection_names())
col=db.get_collection("col")

col.insert({"name":"susan", "time":0})
c=col.find_one({"name":"susan"})
col.update(c, {"$set":{"time":time.time()}})
print(c)
col.find_one().keys()
for c in col.find():
    print(c)
list(col.find())

#col.delete_one({"name":"susan"})
#col.delete_many({"name":"susan"})

print('------------------------or query--------------------------------')
print(col.find_one({"$or":[{"name":"susan"}, {"time":{"$lte":0}}]}))

print('------------------------count--------------------------------')
print(col.count_documents({"name":"susan"}))

'''
Cleanup client resources and disconnect from MongoDB.
On MongoDB >= 3.6, end all server sessions created by this client by sending one or more endSessions commands.
Close all sockets in the connection pools and stop the monitor threads. If this instance is used again it will be automatically re-opened and the threads restarted.
   End all server sessions created by this client. 
'''
conn.close() #as you wish



'''
http://www.runoob.com/mongodb/mongodb-tutorial.html
'''
