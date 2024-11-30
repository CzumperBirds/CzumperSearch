"""Tests for the joke_response_manager context manager."""

import requests
from src.context.joke_context_manager import joke_response_manager


def test_joke_response_manager_success(requests_mock):
    """Test a successful joke response."""
    joke_data = {
        "error": False,
        "joke": "Why did the scarecrow win an award? He was outstanding in his field!",
    }
    requests_mock.get("https://v2.jokeapi.dev/joke/Any", json=joke_data)

    with joke_response_manager() as response:
        assert response == joke_data


def test_joke_response_manager_too_many_requests(requests_mock, mocker):
    """Test handling of TooManyRequestsException."""
    error_response = {
        "error": True,
        "message": "Too Many Requests",
        "code": 429,
        "timestamp": 100,
    }
    headers = {"Retry-After": "2"}
    requests_mock.get(
        "https://v2.jokeapi.dev/joke/Any", json=error_response, headers=headers, status_code=429
    )

    mock_sleep = mocker.patch("time.sleep")

    with joke_response_manager() as response:
        assert response is True
        mock_sleep.assert_called_once_with(2)


def test_joke_response_manager_other_exception(requests_mock):
    """Test handling of other JokeAPIException."""
    error_response = {
        "error": True,
        "message": "Internal Server Error",
        "code": 500,
        "timestamp": 100,
    }
    requests_mock.get("https://v2.jokeapi.dev/joke/Any", json=error_response, status_code=500)

    with joke_response_manager() as response:
        assert response is None


def test_joke_response_manager_network_error(mocker):
    """Test handling of network errors."""
    mocker.patch("requests.get", side_effect=requests.exceptions.ConnectionError)

    with joke_response_manager() as response:
        assert response is None
