from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json
print("START FILE\n")

import time

def wait_for_kafka(consumer, retries=1, delay=5):
    for _ in range(retries):
        try:
            consumer.poll(timeout_ms=1000)  # Check if Kafka is available
            return True
        except Exception as e:
            print(f"Waiting for Kafka... Error: {e}")
            time.sleep(delay)
    return False



consumer = KafkaConsumer(
    'piwo',
    bootstrap_servers='kafka:9092',
    # auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='data-storage-service-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    key_deserializer=lambda x: x.decode('utf-8')

)

if wait_for_kafka(consumer):
    print("Connected to Kafka")
    idx = 0
    for message in consumer:
        print("Message key:", message.key)
        print("Message value:", message.value)
        if idx == 2:
            consumer.close()
        idx +=1
   
else:
    print("Failed to connect to Kafka")

