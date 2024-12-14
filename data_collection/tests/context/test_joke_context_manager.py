"""Tests for the joke_response_manager context manager."""

import pytest
import requests
from src.context.joke_context_manager import joke_response_manager


@pytest.fixture
def _mock_sleep(mocker):
    """Mock time.sleep to avoid delays."""
    mocker.patch("time.sleep", return_value=None)


def test_joke_response_manager_success(requests_mock):
    """Test a successful joke response."""
    joke_data = {
        "error": False,
        "joke": "Why did the scarecrow win an award? He was outstanding in his field!",
    }
    requests_mock.get("https://v2.jokeapi.dev/joke/Any", json=joke_data)

    with joke_response_manager("single") as response:
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

    with joke_response_manager("single") as response:
        assert response is True
        mock_sleep.assert_called_once_with(2)


def test_joke_response_manager_other_exception(requests_mock, _mock_sleep, capfd):
    """Test handling of other JokeAPIException."""
    error_response = {
        "error": True,
        "message": "Internal Server Error",
        "code": 500,
        "timestamp": 100,
    }
    requests_mock.get("https://v2.jokeapi.dev/joke/Any", json=error_response, status_code=500)

    with joke_response_manager("single") as response:
        assert response is True

    out, _ = capfd.readouterr()
    assert (
        "Exception class: <class 'src.exceptions.joke_exception_factory.InternalServerErrorException'>"
        in out
    )
    assert "Additional information: No additional information available." in out
    assert "Retrying after 3 seconds." in out


def test_joke_response_manager_network_error(mocker, _mock_sleep, capfd):
    """Test handling of network errors."""
    mocker.patch("requests.get", side_effect=requests.exceptions.ConnectionError)

    with joke_response_manager("single") as response:
        assert response is True

    out, _ = capfd.readouterr()
    assert "An unexpected error occurred" in out
    assert "Retrying after 3 seconds." in out
