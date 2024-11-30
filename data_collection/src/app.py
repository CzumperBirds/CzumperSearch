"""Module to run the data collection producers."""

import threading
import signal
from src.producers import daily_trivia_producer, joke_producer

RUNNING = True


def signal_handler(sig, frame):
    """Signal handler to stop the producers gracefully."""
    global RUNNING
    print("Received signal to stop. Shutting down producers...")
    RUNNING = False


def run_producer_with_check(produce_function):
    """Run the producer function while checking if the program is still running."""
    global RUNNING
    while RUNNING:
        produce_function()


def main():
    """Main entry point for the data_collection package."""
    threads = []

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    threads.append(threading.Thread(target=run_producer_with_check, args=(joke_producer.produce_jokes,)))
    threads.append(threading.Thread(target=run_producer_with_check, args=(daily_trivia_producer.produce_trivia_fun_facts,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
