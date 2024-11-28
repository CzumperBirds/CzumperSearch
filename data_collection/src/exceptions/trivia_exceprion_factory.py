"""Module for exceptions related to the RSS feed."""


class RSSFeedException(Exception):
    """Base class for exceptions related to the RSS feed."""

    def __init__(self, message: str, details: str = None):
        super().__init__(message)
        self.details = details


class EmptyFeedException(RSSFeedException):
    """Exception raised when the RSS feed has no entries."""


class RSSParseException(RSSFeedException):
    """Exception raised for errors during RSS feed parsing."""
