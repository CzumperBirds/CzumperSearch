# Data Storage Service

The Data Storage Service consumes messages from Kafka topics and stores the processed data into Elasticsearch for further analysis and retrieval.

## Features
* Kafka Consumer: Actively consumes messages from Kafka topics and processes them.

* Elasticsearch Integration: Stores processed messages into Elasticsearch for efficient search and indexing.

* Multi-topic Support: Handles messages from multiple Kafka topics.

* Custom Message Processing: Processes messages based on topic-specific logic before indexing.

## Requirements

* Python 3.13
* Kafka
* Elasticsearch
* Docker (for containerization)

## Instalation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/CzumperBirds/CzumperSearch.git
    cd data_collection
    ```

2. **Install dependencies**:
    ```sh
    make install
    ```

## Setup
**Note** Make sure Kafka and ElasticSearch are running before starting *DataStorageService*

1. **Start Docker Container with --build flag**:
    ```sh
    make up
    ```
  
2. **Start Docker Container (verbose)**:
    ```sh
    make upv
    ```
3. **Stop docker container**
    ```sh
    make down
    ```

4. **Stop docker container and clear volumes**
    ```sh
    make clear
    ```

5. **Get all data from elasticsearch for topic 'processed-resources'**
    ```sh
    make elk_get
    ```

