from kafka import KafkaConsumer
import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.news
consumer = KafkaConsumer('news')

db.news.insert_one({"item": "canvas"})

#for msg in consumer:
#    continue
    # print (msg)

cursor = db.news.find({})
for line in cursor:
    print(line)
