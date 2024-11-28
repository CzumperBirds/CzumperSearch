from kafka import KafkaConsumer, TopicPartition
from elasticsearch import Elasticsearch
import json
import time


class Message:
    def __init__(self, key, value, partition, offset):
        self.key = key
        self.value = value
        self.partition = partition
        self.offset = offset

    def __repr__(self) -> str:
        return f"Message(key={self.key}, value={self.value}, partition={self.partition}, offset={self.offset})"
    
class KafkaHandler:
    """Handles Kafka consumer setup and operations."""
    
    def __init__(self, topic, bootstrap_servers, group_id, auto_offset_reset='earliest'):
        self.topic = topic
        self.bootstrap_servers = bootstrap_servers
        self.group_id = group_id
        self.auto_offset_reset = auto_offset_reset
        self.consumer = None
        

    def setup_consumer(self, value_deserializer, key_deserializer):
        """Initializes the Kafka consumer."""
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=self.bootstrap_servers,
            auto_offset_reset=self.auto_offset_reset,
            enable_auto_commit=False,
            group_id=self.group_id,
            value_deserializer=value_deserializer,
            key_deserializer=key_deserializer
        )
        return self.consumer

    @staticmethod
    def wait_for_kafka(consumer, retries=2, delay=1):
        """Waits for Kafka to be ready, retrying if necessary."""
        for _ in range(retries):
            try:
                consumer.poll(timeout_ms=1000)
                return True
            except Exception as e:
                print(f"Waiting for Kafka... Error: {e}")
                time.sleep(delay)
        return False

    def consume_messages(self, max_messages=None):
        """Consumes messages from the Kafka topic."""
        if not self.consumer:
            raise RuntimeError("Consumer has not been set up. Call setup_consumer first.")
        
        if self.wait_for_kafka(self.consumer):
            print("Connected to Kafka.")
            self.consumer.subscribe([self.topic])
            self.consumer.seek_to_beginning()
            print(f"Subscribed to topic: {self.consumer.subscription()}")
            
            idx = 0
            for message in self.consumer:
                msg = Message(message.key, message.value, message.partition, message.offset)
                yield msg
                # print("Message key:", message.key)
                # print("Message value:", message.value)
                
                idx += 1
                if max_messages and idx >= max_messages:
                    print(f"Consumed {idx} messages. Stopping.")
                    return None
            return True
        else:
            print("Failed to connect to Kafka.")

    @staticmethod
    def consumer_from_offset(topic, group_id, offset, bootstrap_servers):
        """Returns a consumer initialized to a specific offset."""
        consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers, group_id=group_id)
        tp = TopicPartition(topic=topic, partition=0)
        consumer.assign([tp])
        consumer.seek(tp, offset)
        return consumer
    
    def read_from_begining(self, topic=None):
        self.consumer.subscribe([self.topic])
        self.consumer.seek_to_beginning()
        print(f"Subscribed to topic: {self.consumer.subscription()}")


    def close_consumer(self):
        """Closes the Kafka consumer."""
        if self.consumer:
            self.consumer.close()
            print("Consumer closed...")

def main():
    """Main function to initialize and run Kafka consumer."""
    topic = 'piwo'
    bootstrap_servers = 'kafka:9092'
    group_id = 'data-storage-service-group'
    
    kafka_handler = KafkaHandler(topic, bootstrap_servers, group_id)
    
    kafka_handler.setup_consumer(
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        key_deserializer=lambda x: x.decode('utf-8')
    )
    
    print("Consuming messages:")
    for message in kafka_handler.consume_messages(max_messages=3):
        print(message)

    kafka_handler.close_consumer()

    
if __name__ == "__main__":
    print("START FILE\n")
    main()
