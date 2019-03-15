import pymongo
import json
from pprint import pprint

client = pymongo.MongoClient("localhost", 27017)
db = client.news

cursor = db.news.find({})
for line in cursor:
    pprint(line)

