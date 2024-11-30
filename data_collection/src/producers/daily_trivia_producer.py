"""This module contains the function to produce panda articles to Kafka."""

import json
import time
import os
from contextlib import closing
from kafka import KafkaProducer
from src.context.trivia_context_manager import trivia_response_manager
from src.utils.kafka_topic_manager import create_topic, does_topic_exist

KAFKA_ADDRESS = os.getenv("BOOTSTRAP_SERVERS")


def article_generator():
    """Yield articles from the RSS feed."""
    while True:
        with trivia_response_manager() as article:
            if article:
                yield article
            else:
                break


def produce_trivia_fun_facts():
    """Produce trivia fun facts to Kafka."""
    kafka_producer = KafkaProducer(bootstrap_servers=KAFKA_ADDRESS, value_serializer=lambda v: json.dumps(v).encode("utf-8"))

    if not does_topic_exist(topic_name="reddit-daily-trivia", bootstrap_servers=KAFKA_ADDRESS):
        create_topic(topic_name="reddit-daily-trivia", bootstrap_servers=KAFKA_ADDRESS)

    print("Hello from the trivia fun facts producer.")
    with closing(kafka_producer) as kafka:
        for article in article_generator():
            kafka.send("reddit-daily-trivia", article)
            kafka.flush()
            print("Trivia fun fact produced.")
            time.sleep(2)
        print("Goodbye from the trivia fun facts producer.")
