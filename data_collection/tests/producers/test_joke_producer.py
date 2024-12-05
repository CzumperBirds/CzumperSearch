"""Tests for the jokes Kafka producer."""

import pytest
from src.producers.joke_producer import produce_one_part_jokes, produce_two_part_jokes


@pytest.fixture
def mock_kafka_producer(mocker):
    """Mock the KafkaProducer."""
    mock_producer = mocker.patch("src.producers.joke_producer.KafkaProducer")
    return mock_producer.return_value


@pytest.fixture
def mock_sleep(mocker):
    """Mock time.sleep to avoid delays."""
    mocker.patch("time.sleep", return_value=None)


@pytest.fixture
def mock_joke_generator(mocker):
    """Mock the joke generator."""
    mocker.patch(
        "src.producers.joke_producer.joke_generator",
        return_value=iter(
            [
                {"joke": "Why don't skeletons fight? They don't have the guts!"},
                {
                    "joke": "I told my wife she was drawing her eyebrows too high. She looked surprised."
                },
            ]
        ),
    )


def test_produce_one_part_jokes(mock_kafka_producer, mock_joke_generator, mock_sleep, capsys):
    """Test the produce_one_part_jokes function."""
    produce_one_part_jokes()

    # Check that KafkaProducer.send was called with correct arguments
    calls = mock_kafka_producer.send.call_args_list
    assert len(calls) == 2  # Two jokes in mock_joke_generator
    assert calls[0][0][0] == "one-part-jokes"
    assert calls[0][0][1] == {"joke": "Why don't skeletons fight? They don't have the guts!"}
    assert calls[1][0][1] == {
        "joke": "I told my wife she was drawing her eyebrows too high. She looked surprised."
    }

    # Verify printed output
    captured = capsys.readouterr()
    assert "Hello from the jokes producer." in captured.out
    assert "Joke produced." in captured.out
    assert "Goodbye from the jokes producer." in captured.out


def test_produce_two_part_jokes(mock_kafka_producer, mock_joke_generator, mock_sleep, capsys):
    """Test the produce_two_part_jokes function."""
    produce_two_part_jokes()

    # Check that KafkaProducer.send was called with correct arguments
    calls = mock_kafka_producer.send.call_args_list
    assert len(calls) == 2  # Two jokes in mock_joke_generator
    assert calls[0][0][0] == "two-part-jokes"
    assert calls[0][0][1] == {"joke": "Why don't skeletons fight? They don't have the guts!"}
    assert calls[1][0][1] == {
        "joke": "I told my wife she was drawing her eyebrows too high. She looked surprised."
    }

    # Verify printed output
    captured = capsys.readouterr()
    assert "Hello from the jokes producer." in captured.out
    assert "Joke produced." in captured.out
    assert "Goodbye from the jokes producer." in captured.out
