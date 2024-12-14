"""Module to handle joke API responses."""

from contextlib import contextmanager
import time
from src.api.jokes import get_joke_response
from src.exceptions.joke_exception_factory import TooManyRequestsException, JokeAPIException
from src.config import ERROR_WAIT_TIME


@contextmanager
def joke_response_manager(joke_type: str):
    """Context manager to handle joke API responses."""
    try:
        yield get_joke_response(joke_type)
    except TooManyRequestsException as e:
        print(f"Too many requests. Retrying after {e.retry_after} seconds.")
        time.sleep(int(e.retry_after))
        yield True
    except JokeAPIException as e:
        print(f"An error occurred: {e} with code {e.code} (Timestamp: {e.timestamp})")
        print(f"Additional information: {e.info}")
        print(f"Retrying after {ERROR_WAIT_TIME} seconds.")
        time.sleep(ERROR_WAIT_TIME)
        yield True
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print(f"Retrying after {ERROR_WAIT_TIME} seconds.")
        time.sleep(ERROR_WAIT_TIME)
        yield True
