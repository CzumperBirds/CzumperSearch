# Data Search Service (API)

## Overview
Data Search Service is a Spring Boot application that provides an API to search for data stored in
Elasticsearch database with use of full-text searching and with Redis caching.

## Prerequisites
- Java 17 or later
- Maven 4.0.0 or later
- Docker and Docker Compose
- running Elasticsearch database

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/CzumperBirds/CzumperSearch.git
   cd data_search
   ```

## Running the Application

Note: In order to run this service, you need to have the Elasticsearch database running.
It can be set up inside the infrastructure directory. There is a README file with the guide.

### Using Docker Compose

1. **Start the services:**
   ```sh
   docker-compose -f docker-compose.dev.yml up --build
   ```

2. **Access the application:**
   The application will be running on `http://localhost:8081`.

3. Example usage:
   ```sh
   curl http://localhost:8081/api/search?searchPhrase=example
   ```

## Configuration

The application configuration is located in `src/main/resources/application.properties`. Key configurations include:

- **Elasticsearch Configuration:**
  ```ini
  spring.data.elasticsearch.repositories.enabled=true
  spring.elasticsearch.uris=http://elasticsearch:9200
  spring.elasticsearch.username=${ELASTICSEARCH_USERNAME}
  spring.elasticsearch.password=${ELASTICSEARCH_PASSWORD}
  ```

- **Redis Configuration:**
  ```ini
  spring.data.redis.host=localhost
  spring.data.redis.port=6379
  spring.cache.type=redis
  ```

## Usage

### Exposed endpoints

- `/search':
    - GET
    - param: String searchPhrase
    - returns: List of Resources
    - description: Search for resources using full-text searching in Elasticsearch database.
- '/search/content':
    - GET
    - param: String searchPhrase
    - returns: List of Resources
    - description: Search for resources stored in Elasticsearch database by content value.
- `/search/tags`:
    - GET
    - param: String searchPhrase
    - returns: List of Resources
    - description: Search for resources stored in Elasticsearch database by tags value.

