"""This module contains the logic to get a random article from the Reddit Today I Learned RSS feed."""

import os
import random
import feedparser
from src.exceptions.trivia_exceprion_factory import RSSParseException, EmptyFeedException

URL = os.getenv("REDDIT_DAILY_TRIVIA_RSS_URL")


def get_article_response():
    """Get a random article from the RSS feed."""
    feed = feedparser.parse(URL)
    if feed.bozo:
        raise RSSParseException("Failed to parse RSS feed.", details=str(feed.bozo_exception))
    if not feed.entries:
        raise EmptyFeedException(
            "The RSS feed is empty.", details=f"No entries found in the feed. Check the URL: {URL}"
        )
    return random.choice(feed.entries)
