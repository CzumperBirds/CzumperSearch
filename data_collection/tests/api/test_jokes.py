"""Tests for the jokes API."""

import pytest
import requests
from src.api.jokes import get_joke_response
from src.exceptions import joke_exception_factory
from src.config import JOKES_API_URL


def test_get_joke_response_success(requests_mock):
    """Test a successful joke response."""
    joke_data = {
        "error": False,
        "joke": "Why did the scarecrow win an award? He was outstanding in his field!",
    }
    requests_mock.get(JOKES_API_URL, json=joke_data)

    response = get_joke_response()
    assert response == joke_data


@pytest.mark.parametrize(
    "status_code, error_response, exception_type",
    [
        (
            400,
            {"error": True, "message": "Bad Request", "code": 400, "timestamp": 100},
            joke_exception_factory.BadRequestException,
        ),
        (
            403,
            {"error": True, "message": "Forbidden", "code": 403, "timestamp": 100},
            joke_exception_factory.ForbiddenException,
        ),
        (
            404,
            {"error": True, "message": "Not Found", "code": 404, "timestamp": 100},
            joke_exception_factory.NotFoundException,
        ),
        (
            413,
            {"error": True, "message": "Payload Too Large", "code": 413, "timestamp": 100},
            joke_exception_factory.PayloadTooLargeException,
        ),
        (
            414,
            {"error": True, "message": "URI Too Long", "code": 414, "timestamp": 100},
            joke_exception_factory.URITooLongException,
        ),
        (
            429,
            {"error": True, "message": "Too Many Requests", "code": 429, "timestamp": 100},
            joke_exception_factory.TooManyRequestsException,
        ),
        (
            500,
            {"error": True, "message": "Internal Server Error", "code": 500, "timestamp": 100},
            joke_exception_factory.InternalServerErrorException,
        ),
        (
            523,
            {"error": True, "message": "Origin Unreachable", "code": 523, "timestamp": 100},
            joke_exception_factory.OriginUnreachableException,
        ),
    ],
)
def test_get_joke_response_exceptions(requests_mock, status_code, error_response, exception_type):
    """Test that the correct exceptions are raised for various error responses."""
    requests_mock.get(JOKES_API_URL, json=error_response, status_code=status_code)

    with pytest.raises(exception_type) as excinfo:
        get_joke_response()

    exception = excinfo.value
    assert exception.code == error_response["code"]
    assert exception.timestamp is not None
    assert exception.retry_after is None
    assert exception.info == error_response.get(
        "additionalInfo", "No additional information available."
    )
    assert str(exception) == error_response["message"]


def test_get_joke_response_retry_after(requests_mock):
    """Test that Retry-After is included in the exception."""
    error_response = {"error": True, "message": "Too Many Requests", "code": 429, "timestamp": 100}
    headers = {"Retry-After": "120"}
    requests_mock.get(JOKES_API_URL, json=error_response, headers=headers, status_code=429)

    with pytest.raises(joke_exception_factory.TooManyRequestsException) as excinfo:
        get_joke_response()

    exception = excinfo.value
    assert exception.retry_after == "120"


def test_get_joke_response_timeout(mocker):
    """Test that a timeout error raises the appropriate exception."""
    mocker.patch("requests.get", side_effect=requests.exceptions.Timeout)

    with pytest.raises(requests.exceptions.Timeout):
        get_joke_response()


def test_get_joke_response_network_error(mocker):
    """Test that a network error raises the appropriate exception."""
    mocker.patch("requests.get", side_effect=requests.exceptions.ConnectionError)

    with pytest.raises(requests.exceptions.ConnectionError):
        get_joke_response()
