import os
from kafka import KafkaProducer

directory = "dump"

producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic_name = "news"

for filename in os.listdir(directory):
    if filename.endswith(".json"): 
        print(filename)
        with open(directory + "/" + filename) as f:
            file_content = f.read()
            producer.send(topic_name, bytes(file_content, encoding='utf-8'))
    else:
        continue
