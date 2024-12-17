"""This module contains the function to produce jokes to Kafka."""

import json
import time
from contextlib import closing
from kafka import KafkaProducer
from src.api.jokes import get_joke_response
from src.utils.events import collection_paused
from src.config import ERROR_WAIT_TIME, KAFKA_ADDRESS, ONE_PART_JOKES_TOPIC, TWO_PART_JOKES_TOPIC
from src.exceptions.joke_exception_factory import JokeAPIException, TooManyRequestsException


def joke_generator(joke_type: str):
    """Yield jokes from the API."""
    while True:
        collection_paused.wait()
        try:
            yield get_joke_response(joke_type)
        except TooManyRequestsException as e:
            print(f"Too many requests. Retrying after {e.retry_after} seconds.")
            time.sleep(int(e.retry_after))
        except JokeAPIException as e:
            print(f"An error occurred: {e} with code {e.code} (Timestamp: {e.timestamp})")
            print(f"Additional information: {e.info}")
            print(f"Retrying after {ERROR_WAIT_TIME} seconds.")
            time.sleep(ERROR_WAIT_TIME)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print(f"Retrying after {ERROR_WAIT_TIME} seconds.")
            time.sleep(ERROR_WAIT_TIME)


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
        kafka.close()
        print("Goodbye from the jokes producer.")
