# CzumperSearch

CzumperSearch is a microservices-based application designed to collect, process, and search data from various sources. The project is divided into several services, each responsible for a specific part of the workflow.

## Authors
- Oliwier Szypczyn
- Artur Kempiński
- Mateusz Matkiewiszcz
- Kacper Multan
- Jakub Kryczka

## Overview

The CzumperSearch project consists of the following microservices:

1. **Data Collection**: Collects data from external sources and produces messages to Kafka topics.
2. **Data Processor**: Consumes messages from Kafka topics, processes them, and produces processed messages to another Kafka topic.
3. **Data Storage**: Stores processed data in Elasticsearch and provides an API for data retrieval.
4. **Data Search**: Provides search capabilities over the stored data using Elasticsearch.
5. **Frontend**: A web application that allows users to search and view the collected data.

## Microservices

### Data Collection

- **Description**: Collects data from various sources such as APIs and RSS feeds.
- **Technologies**: Python, FastAPI, Kafka
- **Repository**: [data_collection](data_collection/README.md)

### Data Processor

- **Description**: Processes the collected data and produces processed messages to Kafka topics.
- **Technologies**: Java, Spring Boot, Kafka, MongoDB
- **Repository**: [data_processor](data_processor/README.md)

### Data Storage

- **Description**: Stores processed data in Elasticsearch and provides an API for data retrieval.
- **Technologies**: Python, Elasticsearch, Kafka
- **Repository**: [data_storage](data_storage/README.md)

### Data Search

- **Description**: Provides search capabilities over the stored data using Elasticsearch.
- **Technologies**: Java, Spring Boot, Elasticsearch, Redis
- **Repository**: [data_search](data_search/README.md)

### Frontend

- **Description**: A web application that allows users to search and view the collected data.
- **Technologies**: Angular, TypeScript, Node.js
- **Repository**: [frontend](frontend/CzumperSearch/README.md)

## Infrastructure

The project uses Docker and Docker Compose for containerization and orchestration. The infrastructure setup includes Kafka, Elasticsearch, Redis, and other necessary services.

- **Development Environment**: [docker-compose.dev.yml](infrastructure/docker-compose.dev.yml)
- **Test Environment**: [docker-compose.test.yml](infrastructure/docker-compose.test.yml)

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Running the Application

1. **Clone the repository**:
    ```bash
    git clone https://github.com/CzumperBirds/CzumperSearch.git
    cd CzumperSearch
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.