#!/bin/bash
# Launch Mongo
sudo systemctl start mongodb.service

sudo systemctl start kafka.service

# Launch Kafka
sudo kafka-server-start.sh config/server.properties

