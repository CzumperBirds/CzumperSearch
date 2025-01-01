# Data Processor Service

## Overview
The Data Processor Service is a Spring Boot application that consumes messages from Kafka topics and processes them. It also produces processed messages to another Kafka topic.

## Prerequisites
- Java 17 or later
- Maven 3.9.9 or later
- Docker and Docker Compose

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/CzumperBirds/CzumperSearch.git
   cd data_processor_service
   ```

2. **Run tests:**
   ```sh
   mvn test
   ```

## Running the Application

Note: In order to run this service, you need to have the Kafka server running. It can be set up inside the infrastructure directory. There is a README file with the guide.  Additionally, it is recommended to have some raw messages inside Kafka. To achieve this, you can run the data_collection service. Instructions on how to do this are available inside the data_collection README.md file.

### Using Docker Compose

1. **Start the services:**
   ```sh
   docker-compose -f docker-compose.dev.yml up --build
   ```

2. **Access the application:**
   The application will be running on `http://localhost:8080`.

## Configuration

The application configuration is located in `src/main/resources/application.properties`. Key configurations include:

- **Kafka Configuration:**
  ```ini
  spring.kafka.bootstrap-servers=kafka:9092
  spring.kafka.consumer.group-id=spring-middleman
  spring.kafka.consumer.auto-offset-reset=earliest
  ```

- **MongoDB Configuration:**
  ```ini
  spring.data.mongodb.host=mongo
  spring.data.mongodb.port=27017
  spring.data.mongodb.database=processed_resources_db
  ```

## Usage

### Kafka Consumers

The application listens to the following Kafka topics:

- `daily-trivia`
- `one-part-jokes`
- `two-part-jokes`

### Kafka Producers

Processed messages are sent to the `processed-resources` topic.

### MongoDB Collections

Processed data is stored in the following MongoDB collections to avoid processing the same data multiple times:

- `daily_trivia`
- `one_part_jokes`
- `two_part_jokes`
