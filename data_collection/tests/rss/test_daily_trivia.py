"""Tests for the daily trivia API."""

from unittest.mock import MagicMock, patch
import pytest
import requests
from src.rss.daily_trivia import get_article_response
from src.exceptions.trivia_exceprion_factory import RSSParseException, EmptyFeedException


@pytest.fixture
def mock_rss_response():
    """Mock the RSS feed response with required properties."""
    mock_feed = MagicMock()
    mock_feed.bozo = False
    mock_feed.entries = [
        {
            "title": "Today I Learned",
            "link": "https://www.reddit.com/r/todayilearned/comments/xyz",
            "published": "2024-11-30T23:15:11Z",
        }
    ]
    mock_feed.bozo_exception = None
    return mock_feed


@pytest.fixture
def mock_empty_rss_response():
    """Mock the RSS feed response with no entries."""
    mock_feed = MagicMock()
    mock_feed.bozo = False
    mock_feed.entries = []
    mock_feed.bozo_exception = None
    return mock_feed


@pytest.fixture
def mock_rss_parse_error():
    """Mock the RSS feed response with a parse error."""
    mock_feed = MagicMock()
    mock_feed.bozo = True
    mock_feed.entries = []
    mock_feed.bozo_exception = Exception("Invalid RSS feed")
    return mock_feed


def test_get_article_response_success(mock_rss_response):
    """Test a successful article response."""

    with patch("feedparser.parse", return_value=mock_rss_response):
        response = get_article_response()

    expected_response = {
        "title": "Today I Learned",
        "link": "https://www.reddit.com/r/todayilearned/comments/xyz",
        "published": "2024-11-30T23:15:11Z",
    }
    assert response == expected_response


def test_get_article_response_empty_feed(mock_empty_rss_response):
    """Test handling of an empty feed."""
    with patch("feedparser.parse", return_value=mock_empty_rss_response):
        with pytest.raises(EmptyFeedException) as excinfo:
            get_article_response()

    exception = excinfo.value
    assert str(exception) == "The RSS feed is empty."
    assert "No entries found in the feed." in exception.details


def test_get_article_response_rss_parse_exception(mock_rss_parse_error):
    """Test handling of an RSS parse exception."""
    with patch("feedparser.parse", return_value=mock_rss_parse_error):
        with pytest.raises(RSSParseException) as excinfo:
            get_article_response()

    exception = excinfo.value
    assert str(exception) == "Failed to parse RSS feed."
    assert "Invalid RSS feed" in exception.details


def test_get_article_response_timeout(mocker):
    """Test that a timeout error raises the appropriate exception."""
    mocker.patch("feedparser.parse", side_effect=requests.exceptions.Timeout)

    with pytest.raises(requests.exceptions.Timeout):
        get_article_response()


def test_get_article_response_network_error(mocker):
    """Test that a network error raises the appropriate exception."""
    mocker.patch("feedparser.parse", side_effect=requests.exceptions.ConnectionError)

    with pytest.raises(requests.exceptions.ConnectionError):
        get_article_response()
