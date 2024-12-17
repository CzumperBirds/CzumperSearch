"""This module manages the message producing threads."""

import threading
from src.producers import daily_trivia_producer, joke_producer
import src.config
from src.utils.events import collection_paused

producer_threads = []


def init_producers():
    collection_paused.clear()

    producer_threads.append(threading.Thread(target=joke_producer.produce_one_part_jokes))
    producer_threads.append(threading.Thread(target=joke_producer.produce_two_part_jokes))
    producer_threads.append(threading.Thread(target=daily_trivia_producer.produce_trivia_fun_facts))

    for thread in producer_threads:
        thread.start()


def start_producers():
    """Start the message producing threads."""
    if src.config.RUNNING:
        print("Producers already running")
        return

    src.config.RUNNING = True
    collection_paused.set()

    print("Starting producers...")


def pause_producers():
    """Pause the message producing threads."""
    if not src.config.RUNNING:
        print("Producers are already not running")
        return

    src.config.RUNNING = False
    collection_paused.clear()

    print("Pausing producers...")


def stop_producers():
    """Stop the message producing threads."""
    collection_paused.set()

    for thread in producer_threads:
        thread.join()

    print("Stopping producers...")
