"""This module contains the function to produce jokes to Kafka."""

import json
from kafka import KafkaProducer
from decouple import config
from src.context.joke_context_manager import joke_response_manager

KAFKA_ADDRESS = config("KAFKA_ADDRESS")


def produce_jokes():
    """Function to get joke response and send it to Kafka."""
    kafka_producer = KafkaProducer(
        bootstrap_servers=KAFKA_ADDRESS, value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    print("Hello from joke producer.")
    while True:
        with joke_response_manager() as joke:
            if joke:
                kafka_producer.send("jokes", joke)
                kafka_producer.flush()
                print("Joke produced.")
            else:
                break
