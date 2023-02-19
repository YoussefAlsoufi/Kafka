from kafka import KafkaConsumer
import json


if __name__ == "__main__":
    consumer= KafkaConsumer("Youssef_Topic_2", bootstrap_servers='10.1.5.0:9092',
                            auto_offset_reset='earliest',group_id="Consumer_Group_1")
    print("The Consumer started")
    for msg in consumer:
        print ("Consumer received a message!")
        print ("From Youssef_Topic_2 : {} ".format(json.loads(msg.value)))
        #print (json.load(msg.value))


  