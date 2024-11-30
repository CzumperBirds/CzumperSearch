"""This module manages the message producing threads."""

import threading
from src.producers import daily_trivia_producer, joke_producer
import src.config

producer_threads = []


def start_producers():
    """Start the message producing threads."""
    print("Starting producers...")
    global producer_threads
    src.config.RUNNING = True

    producer_threads.append(threading.Thread(target=joke_producer.produce_jokes))
    producer_threads.append(threading.Thread(target=daily_trivia_producer.produce_trivia_fun_facts))

    for thread in producer_threads:
        thread.start()


def stop_producers():
    """Stop the message producing threads."""
    print("Stopping producers...")
    global producer_threads

    if src.config.RUNNING:
        src.config.RUNNING = False

        for thread in producer_threads:
            thread.join()

        producer_threads.clear()
        print("Producers stopped.")
