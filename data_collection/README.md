# Data Collection App

This application collects data from various sources and produces messages to Kafka topics. It includes producers for daily trivia and jokes.

## Features

- **Daily Trivia Producer**: Fetches random articles from the Reddit Today I Learned RSS feed and sends them to a Kafka topic.
- **Jokes Producer**: Fetches jokes from an API and sends them to a Kafka topic.
- **Graceful Shutdown**: Handles signals to stop the producers gracefully.

## Requirements

- Python 3.13
- Kafka
- Docker (for containerization)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/CzumperBirds/CzumperSearch.git
    cd data_collection
    ```

## Running with Docker

1. **Build and run the Docker image**:
    ```bash
    docker compose up --build
    ```

## Managing the process of message factory

1. **Stop the message producing**:
    ```bash
    curl -X 'POST' \
    'http://localhost:8000/control' \
    -H 'Content-Type: application/json' \
    -d '{"action": "stop"}'
    ```

2. **Restart the message producing again**:
    ```bash
    curl -X 'POST' \
    'http://localhost:8000/control' \
    -H 'Content-Type: application/json' \
    -d '{"action": "start"}'
    ```