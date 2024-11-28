"""Main entry point for the data_collection package."""

import threading
from src.producers import daily_trivia_producer, joke_producer


def main():
    """Main entry point for the data_collection package."""
    threads = []

    threads.append(threading.Thread(target=joke_producer.produce_jokes))
    threads.append(threading.Thread(target=daily_trivia_producer.produce_trivia_fun_facts))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
