"""Main entry point for the data_collection package."""

import threading
from src.producers.joke_producer import produce_jokes


def main():
    """Main entry point for the data_collection package."""
    joke_thread = threading.Thread(target=produce_jokes)
    joke_thread.start()
    joke_thread.join()


if __name__ == "__main__":
    main()
