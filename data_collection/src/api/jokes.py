"""Module to get jokes from jokeapi.dev"""

import requests
from src.exceptions.joke_exception_factory import get_joke_api_exception
from src.config import JOKES_API_URL, TIMEOUT


def get_joke_response() -> dict:
    """Get a joke from jokeapi.dev"""
    response = requests.get(JOKES_API_URL, timeout=TIMEOUT)
    error_occured = response.json().get("error", False)
    if error_occured:
        raise get_joke_api_exception(response.json(), response.headers)
    return response.json()
