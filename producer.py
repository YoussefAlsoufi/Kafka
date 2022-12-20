# Kafka Server:
# The task: create a single broker with one partition;
# All the messages will be published to as single partition;

from kafka import KafkaProducer
import json
from dataToPublish import registered_user
import time

def json_serializer(published_data):
    return json.dumps(published_data).encode("utf-8")

#def GetSpecificPartion(key,all,availablePartition):
#    return 2

#producer= KafkaProducer(bootstrap_servers=['10.1.5.0:9092'], value_serializer=json_serializer,
#                        partitioner= GetSpecificPartion)

producer= KafkaProducer(bootstrap_servers=['10.1.5.0:9092'], value_serializer=json_serializer)

if __name__ == "__main__":
    while True:
        data = registered_user()
        producer.send("Youssef_Topic_2",data)
        print(data)
        time.sleep(4) 
        