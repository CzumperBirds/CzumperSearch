"""This module contains the function to produce panda articles to Kafka."""

import json
import time
from contextlib import closing
from kafka import KafkaProducer
from src.context.trivia_context_manager import trivia_response_manager
import src.config
from src.config import KAFKA_ADDRESS, DAILY_TRIVIA_TOPIC


def article_generator():
    """Yield articles from the RSS feed."""
    while src.config.RUNNING:
        with trivia_response_manager() as article:
            if article:
                yield article
            else:
                break


def produce_trivia_fun_facts():
    """Produce trivia fun facts to Kafka."""
    kafka_producer = KafkaProducer(
        bootstrap_servers=KAFKA_ADDRESS, value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )

    print("Hello from the trivia fun facts producer.")
    with closing(kafka_producer) as kafka:
        for article in article_generator():
            kafka.send(DAILY_TRIVIA_TOPIC, article)
            kafka.flush()
            print("Trivia fun fact produced.")
            time.sleep(2)
        print("Goodbye from the trivia fun facts producer.")
