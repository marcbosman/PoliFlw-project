#!/bin/bash
# Launch zookeeper
# urxvt -e "systemctl start mongodb.service"

# Launch Kafka
sudo sh kafka-server-start.sh config/server.properties &

sleep 100

# Create topics
kafka-topics.sh --create \
    --zookeeper localhost:2181 \
    --replication-factor 1 \
    --partitions 1 \
    --topic news

