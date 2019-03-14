from kafka import KafkaConsumer
import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.news
consumer = KafkaConsumer('news')


db.createCollection("news")

db.news.insert_many([{"item": "canvas"}, {"something", "cool shit"}])

for msg in consumer:
    continue
    # print (msg)

cursor = db.news.find({})
print(cursor)
