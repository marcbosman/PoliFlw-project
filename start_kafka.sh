#!/bin/bash
# Launch Mongo
sudo systemctl start mongodb.service

# Launch Kafka
sudo sh kafka-server-start.sh config/server.properties

