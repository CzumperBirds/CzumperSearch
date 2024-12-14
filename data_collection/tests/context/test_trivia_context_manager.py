"""Tests for the trivia context manager."""

from unittest.mock import MagicMock
import pytest
from src.context.trivia_context_manager import trivia_response_manager


@pytest.fixture
def _mock_sleep(mocker):
    """Mock time.sleep to avoid delays."""
    mocker.patch("time.sleep", return_value=None)


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
    mock_feed.bozo_exception = Exception("Exception details")
    return mock_feed


@pytest.fixture
def mock_rss_parse_error():
    """Mock the RSS feed response with a parse error."""
    mock_feed = MagicMock()
    mock_feed.bozo = True
    mock_feed.entries = []
    mock_feed.bozo_exception = Exception("Exception details")
    return mock_feed


def test_trivia_response_manager_success(mocker, mock_rss_response):
    """Test a successful trivia response."""
    mocker.patch("feedparser.parse", return_value=mock_rss_response)

    with trivia_response_manager() as response:
        assert response == mock_rss_response.entries[0]


def test_trivia_response_manager_no_entries(mocker, mock_empty_rss_response, capsys, _mock_sleep):
    """Test handling of no entries in the RSS feed."""
    mocker.patch("feedparser.parse", return_value=mock_empty_rss_response)

    with trivia_response_manager() as response:
        assert response is True

    captured = capsys.readouterr()
    assert "RSS feed is empty" in captured.out
    assert "No entries found in the feed. Check the URL" in captured.out


def test_trivia_response_manager_parse_error(mocker, mock_rss_parse_error, capsys, _mock_sleep):
    """Test handling of a parse error in the RSS feed."""
    mocker.patch("feedparser.parse", return_value=mock_rss_parse_error)

    with trivia_response_manager() as response:
        assert response is True

    captured = capsys.readouterr()
    assert "Failed to parse RSS feed" in captured.out
    assert "Exception details" in captured.out
