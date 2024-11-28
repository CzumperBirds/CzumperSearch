from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json
print("START FILE")


es = Elasticsearch(['http://elasticsearch:9200'])  # Elasticsearch service inside the Docker network
print("1")

consumer = KafkaConsumer(
    'piwo_woda_polibuda',
    bootstrap_servers=['kafka:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='data-storage-service-group',

)

# if __name__ == '__main__':
print("Data Storage Service started")
try:
    print("TRY")
    for message in consumer:
        print("Message")
#             record = json.loads(message.value.decode('utf-8'))
#             print(f"Received message: {record}")
except Exception as e:
    print(f"Error: {e}")
#     # Insert into Elasticsearch
#     es.index(index='your_index_name', document=record)
#     print(f"Inserted record into Elasticsearch: {record}")
finally:
    consumer.close()
    print("Data Storage Service stopped")
