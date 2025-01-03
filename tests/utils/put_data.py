import os
from kafka import KafkaProducer
import json
from datetime import datetime
import random

# Function to create the DailyTriviaConsumed structure
def create_daily_trivia_data():
    trivia_data = {
        "id": f"trivia-{random.randint(1, 10000)}",
        "title": "randomtestdata",
        "link": "https://example.com/trivia-link",
        "author": "Trivia Author",
        "published": datetime.now().isoformat(),  # ISO 8601 format for current datetime
        "tags": [
            {"category": "Science"},
            {"category": "History"},
            {"category": "Pop Culture"}
        ]
    }
    return trivia_data

# Function to send data to Kafka
def send_to_kafka():
    bootstrap_servers = os.getenv('BOOTSTRAP_SERVERS', 'kafka:9092')
    # Kafka producer configuration
    producer = KafkaProducer(
        bootstrap_servers=[bootstrap_servers],  # Use the environment variable
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    topic = "daily-trivia"

    # Prepare data
    data = create_daily_trivia_data()

    # Send data to Kafka topic "daily-trivia"
    producer.send(topic, data)
    print(f"Sent data to Kafka: {data}")

    # Close the producer connection
    producer.flush()
    producer.close()

if __name__ == "__main__":
    send_to_kafka()