"""Tests for the producer_manager module."""

from unittest.mock import patch
import time
import threading
import pytest
from src.utils.producer_manager import (
    init_producers,
    start_producers,
    pause_producers,
    producer_threads,
    stop_producers,
)
import src.config


@pytest.fixture(autouse=True)
def reset_producer_threads():
    """Ensure producer_threads is reset before each test."""
    producer_threads.clear()


def test_start_producers():
    """Test that start_producers correctly starts threads."""

    def mock_produce_jokes():
        while src.config.RUNNING:
            time.sleep(0.3)

    def mock_produce_trivia_fun_facts():
        while src.config.RUNNING:
            time.sleep(0.3)

    with patch(
        "src.producers.joke_producer.produce_one_part_jokes", side_effect=mock_produce_jokes
    ), patch(
        "src.producers.daily_trivia_producer.produce_trivia_fun_facts",
        side_effect=mock_produce_trivia_fun_facts,
    ), patch(
        "src.producers.joke_producer.produce_two_part_jokes", return_value=mock_produce_jokes
    ):
        init_producers()

        assert len(producer_threads) == 3
        assert all(isinstance(thread, threading.Thread) for thread in producer_threads)
        for thread in producer_threads:
            assert thread.is_alive()

        for thread in producer_threads:
            thread.join()


def test_stop_producers():
    """Test that stop_producers correctly stops threads."""
    with patch("src.producers.joke_producer.produce_one_part_jokes", return_value=None), patch(
        "src.producers.daily_trivia_producer.produce_trivia_fun_facts", return_value=None
    ), patch("src.producers.joke_producer.produce_two_part_jokes", return_value=None):
        init_producers()

        assert len(producer_threads) == 3

        stop_producers()

        assert len(producer_threads) == 0
