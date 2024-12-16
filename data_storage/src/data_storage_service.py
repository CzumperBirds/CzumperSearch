from kafka import KafkaConsumer
import json
from elastic_handler import ElasticsearchHandler
from pprint import pprint

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

    def consume_messages(self):
        """Consumes messages from the Kafka topic."""
        if not self.consumer:
            raise RuntimeError("Consumer has not been set up. Call setup_consumer first.")
        
        for message in self.consumer:
            yield {
                "key": message.key,
                "value": message.value,
                "partition": message.partition,
                "offset": message.offset
            }


def process_and_index_message(topic, message, es_handler):
    """Processes a message based on its topic and indexes it into Elasticsearch."""
    if topic == "processed-resources":
        value = message["value"]
        document = {
            "type": value.get("type"),
            "source": value.get("source"),
            "content": value.get("content"),
            "published": value.get("published"),
            "tags": value.get("tags")
        }
        index_name = "processed-resources"
    
    else:
        print(f"Unknown topic: {topic}")
        return None
    
    return es_handler.index_message(index_name, document)


def main():
    """Main function to initialize and run Kafka consumer."""
    topics = ['processed-resources']
    bootstrap_servers = 'kafka:9092'
    group_id = 'data-storage-service-group'
    elasticsearch_url = "http://elasticsearch:9200"
    
    es_handler = ElasticsearchHandler(elasticsearch_url)
    
    for topic in topics:
        kafka_handler = KafkaHandler(topic, bootstrap_servers, group_id)
        kafka_handler.setup_consumer(
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
            key_deserializer=lambda x: x.decode('utf-8') if x else None
        )
        
        print(f"Consuming messages from topic: {topic}")
        
        for message in kafka_handler.consume_messages():
            print(f"Processing message: {message}")
            
            es_response = process_and_index_message(topic, message, es_handler)
            if es_response:
                print(f"Indexed to Elasticsearch: {es_response}")
        
        kafka_handler.close_consumer()

if __name__ == "__main__":
    main()
