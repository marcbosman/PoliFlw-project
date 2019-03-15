from kafka import KafkaConsumer
import pymongo
import analyze

client = pymongo.MongoClient("localhost", 27017)
db = client.news
consumer = KafkaConsumer('news')


for msg in consumer:
    source = msg.value.decode("utf-8") 
    parsed = analyze.getWords(source)
    db.news.insert_one(parsed)

cursor = db.news.find({})
for line in cursor:
    print(line)
