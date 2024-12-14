"""Context manager to handle RSS feed responses."""

import time
from contextlib import contextmanager
from src.rss.daily_trivia import get_article_response
from src.exceptions.trivia_exceprion_factory import (
    EmptyFeedException,
    RSSParseException,
)
from src.config import ERROR_WAIT_TIME


@contextmanager
def trivia_response_manager():
    """Context manager to handle RSS feed responses."""
    try:
        yield get_article_response()
    except EmptyFeedException as e:
        print(f"RSS feed is empty: {e}")
        print("Details:", e.details)
        print(f"Retrying after {ERROR_WAIT_TIME} seconds.")
        time.sleep(ERROR_WAIT_TIME)
        yield True
    except RSSParseException as e:
        print(f"Failed to parse RSS feed: {e}")
        print("Details:", e.details)
        print(f"Retrying after {ERROR_WAIT_TIME} seconds.")
        time.sleep(ERROR_WAIT_TIME)
        yield True
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print(f"Retrying after {ERROR_WAIT_TIME} seconds.")
        time.sleep(ERROR_WAIT_TIME)
        yield True
