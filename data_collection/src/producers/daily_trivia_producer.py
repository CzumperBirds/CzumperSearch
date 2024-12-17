"""This module contains the function to produce panda articles to Kafka."""

import json
import time
from contextlib import closing
from kafka import KafkaProducer
from src.config import ERROR_WAIT_TIME, KAFKA_ADDRESS, DAILY_TRIVIA_TOPIC
from src.exceptions.trivia_exceprion_factory import EmptyFeedException, RSSParseException
from src.rss.daily_trivia import get_article_response
from src.utils.events import collection_paused


def article_generator():
    """Yield articles from the RSS feed."""
    while True:
        collection_paused.wait()
        try:
            yield get_article_response()
        except EmptyFeedException as e:
            print(f"RSS feed is empty: {e}")
            print("Details:", e.details)
            print(f"Retrying after {ERROR_WAIT_TIME} seconds.")
            time.sleep(ERROR_WAIT_TIME)
        except RSSParseException as e:
            print(f"Failed to parse RSS feed: {e}")
            print("Details:", e.details)
            print(f"Retrying after {ERROR_WAIT_TIME} seconds.")
            time.sleep(ERROR_WAIT_TIME)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print(f"Retrying after {ERROR_WAIT_TIME} seconds.")
            time.sleep(ERROR_WAIT_TIME)


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
        kafka.close()
        print("Goodbye from the trivia fun facts producer.")
