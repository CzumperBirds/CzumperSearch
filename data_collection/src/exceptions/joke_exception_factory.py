"""Module for exceptions from jokeapi.dev"""

from datetime import datetime

from requests import Response


def get_joke_api_exception(response: Response) -> Exception:
    """Get the appropriate exception based on the response."""
    body = response.json()
    error_message = body.get("message", "An error occurred with the joke API.")
    code = int(body.get("code", 500))
    raw_timestamp = body.get("timestamp")
    if raw_timestamp is not None:
        timestamp = datetime.fromtimestamp(raw_timestamp / 1000).strftime("%Y-%m-%d %H:%M:%S")
    else:
        timestamp = None
    info = body.get("additionalInfo", "No additional information available.")

    exception_map = {
        101: TooManyRequestsException,
        400: BadRequestException,
        403: ForbiddenException,
        404: NotFoundException,
        413: PayloadTooLargeException,
        414: URITooLongException,
        429: TooManyRequestsException,
        500: InternalServerErrorException,
        523: OriginUnreachableException,
    }

    exception_class = exception_map.get(code, JokeAPIException)
    print(f"Exception class: {exception_class}")
    return exception_class(
        message=error_message,
        code=code,
        timestamp=timestamp,
        retry_after=response.headers.get("Retry-After"),
        info=info,
    )


class JokeAPIException(Exception):
    """Base class for exceptions from jokeapi.dev"""

    def __init__(self, message: str, code: int, timestamp: str, retry_after: str, info: str):
        super().__init__(message)
        self.timestamp = timestamp
        self.retry_after = retry_after
        self.code = code
        self.info = info


class BadRequestException(JokeAPIException):
    """Exception for 400 Bad Request"""


class ForbiddenException(JokeAPIException):
    """Exception for 403 Forbidden"""


class NotFoundException(JokeAPIException):
    """Exception for 404 Not Found"""


class PayloadTooLargeException(JokeAPIException):
    """Exception for 413 Payload Too Large"""


class URITooLongException(JokeAPIException):
    """Exception for 414 URI Too Long"""


class TooManyRequestsException(JokeAPIException):
    """Exception for 429 Too Many Requests"""


class InternalServerErrorException(JokeAPIException):
    """Exception for 500 Internal Server Error"""


class OriginUnreachableException(JokeAPIException):
    """Exception for 523 Origin Unreachable"""
