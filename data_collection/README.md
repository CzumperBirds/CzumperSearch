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

2. **Stop the message producing**:
    ```bash
    docker stop poetry-kafka-producer
    ```

3. **Start the message producing again**:
    ```bash
    docker start poetry-kafka-producer
    ```