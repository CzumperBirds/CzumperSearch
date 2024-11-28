"""This module contains the function to produce jokes to Kafka."""

import json
import os
import time
from contextlib import closing
from kafka import KafkaProducer
from src.context.joke_context_manager import joke_response_manager

KAFKA_ADDRESS = os.getenv("BOOTSTRAP_SERVERS")


def joke_generator():
    """Yield jokes from the API."""
    while True:
        with joke_response_manager() as joke:
            if joke:
                yield joke
            else:
                break


def produce_jokes():
    """Function to get joke response and send it to Kafka."""
    kafka_producer = KafkaProducer(
        bootstrap_servers=KAFKA_ADDRESS, value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )

    print("Hello from the jokes producer.")
    with closing(kafka_producer) as kafka:
        for joke in joke_generator():
            kafka.send("jokes", joke)
            kafka.flush()
            print("Joke produced.")
            time.sleep(2)
        print("Goodbye from the jokes producer.")
