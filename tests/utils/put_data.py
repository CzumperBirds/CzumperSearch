import os
from kafka import KafkaProducer
import json
from datetime import datetime
import random

# Function to create the DailyTriviaConsumed structure
def create_daily_trivia_data():
    trivia_data = {
        "id": f"trivia-test-12312df4141-190234",
        "title": "randomtestdata",
        "link": "https://example.com/trivia-link",
        "author": "Trivia Author",
        "published": "2025-01-03T10:15:30+01:00",
        "tags": [
            {"category": "Science"},
            {"another": "History"},
            {"test": "Pop Culture"}
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