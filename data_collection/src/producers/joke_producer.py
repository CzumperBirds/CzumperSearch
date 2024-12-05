"""This module contains the function to produce jokes to Kafka."""

import json
import time
from contextlib import closing
from kafka import KafkaProducer
from src.context.joke_context_manager import joke_response_manager
import src.config
from src.config import KAFKA_ADDRESS, ONE_PART_JOKES_TOPIC, TWO_PART_JOKES_TOPIC


def joke_generator(joke_type: str):
    """Yield jokes from the API."""
    while src.config.RUNNING:
        with joke_response_manager(joke_type) as joke:
            if joke:
                yield joke
            else:
                break


def produce_one_part_jokes():
    """Function to produce one part jokes to Kafka."""
    produce_jokes(topic_name=ONE_PART_JOKES_TOPIC, joke_type="single")


def produce_two_part_jokes():
    """Function to produce two part jokes to Kafka."""
    produce_jokes(topic_name=TWO_PART_JOKES_TOPIC, joke_type="twopart")


def produce_jokes(topic_name: str, joke_type: str):
    """Function to get joke response and send it to Kafka."""
    kafka_producer = KafkaProducer(
        bootstrap_servers=KAFKA_ADDRESS, value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )

    print("Hello from the jokes producer.")
    with closing(kafka_producer) as kafka:
        for joke in joke_generator(joke_type):
            kafka.send(topic_name, joke)
            kafka.flush()
            print("Joke produced.")
            time.sleep(2)
        print("Goodbye from the jokes producer.")
