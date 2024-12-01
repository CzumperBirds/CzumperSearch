"""Tests for the daily trivia Kafka producer."""

import pytest
from src.producers.daily_trivia_producer import produce_trivia_fun_facts


@pytest.fixture
def mock_kafka_producer(mocker):
    """Mock the KafkaProducer."""
    mock_producer = mocker.patch("src.producers.daily_trivia_producer.KafkaProducer")
    return mock_producer.return_value


@pytest.fixture
def mock_topic_functions(mocker):
    """Mock Kafka topic management functions."""
    mocker.patch("src.producers.daily_trivia_producer.does_topic_exist", return_value=False)
    mock_create_topic = mocker.patch("src.producers.daily_trivia_producer.create_topic")
    return mock_create_topic


@pytest.fixture
def mock_sleep(mocker):
    """Mock time.sleep to avoid delays."""
    mocker.patch("time.sleep", return_value=None)


@pytest.fixture
def mock_article_generator(mocker):
    """Mock the article generator."""
    mocker.patch(
        "src.producers.daily_trivia_producer.article_generator",
        return_value=iter(
            [
                {"trivia": "The first oranges weren't orange."},
                {"trivia": "The shortest war in history lasted 38 minutes."},
            ]
        ),
    )


def test_produce_trivia_fun_facts(
    mock_kafka_producer, mock_topic_functions, mock_article_generator, mock_sleep
):
    """Test the produce_trivia_fun_facts function."""
    produce_trivia_fun_facts()

    # Check that the topic creation function was called
    mock_topic_functions.assert_called_once_with(
        topic_name="reddit-daily-trivia", bootstrap_servers="localhost:9092"
    )

    calls = mock_kafka_producer.send.call_args_list
    assert len(calls) == 2
    assert calls[0][0][0] == "reddit-daily-trivia"
    assert calls[0][0][1] == {"trivia": "The first oranges weren't orange."}
    assert calls[1][0][1] == {"trivia": "The shortest war in history lasted 38 minutes."}


def test_produce_daily_tivia_no_topic_creation(mocker, mock_kafka_producer):
    """Test the produce_trivia_fun_facts function when the topic already exists."""
    mocker.patch("src.producers.daily_trivia_producer.does_topic_exist", return_value=True)

    produce_trivia_fun_facts()

    # Check that the topic creation function was not called
    mock_kafka_producer.assert_not_called()
