#FROM maven:3-amazoncorretto-21 AS build
#
#RUN apt-get update && apt-get install -y --no-install-recommends \
#    build-essential libpq-dev curl \
#    && apt-get clean \
#    && rm -rf /var/lib/apt/lists/* \
#
#WORKDIR /app
#COPY pom.xml .
#COPY src ./src
#
#RUN mvn clean package -DskipTests
#RUN mvn wrapper:wrapper
#
#FROM amazoncorretto:21
#WORKDIR /app
#
#COPY --from=build /app/target/dataSearchService.jar .
#
#RUN chmod +x /app//wait-for-elasticsearch.sh
#ENTRYPOINT ["/app/wait-for-elasticsearch.sh"]
#
#EXPOSE 8080
#CMD ["java", "-jar", "dataSearchService.jar"]

# Use an official Ubuntu image as the base image
FROM ubuntu:20.04

# Set environment variables to reduce interaction during setup
ENV DEBIAN_FRONTEND=noninteractive

# Update the package repository and install required packages
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk maven curl git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy your application's source code into the container
COPY ../../CzumpersSearch/data_search .

# Optionally run Maven commands to build the project
RUN mvn clean package

RUN chmod +x /app//wait-for-elasticsearch.sh
ENTRYPOINT ["/app/wait-for-elasticsearch.sh"]


EXPOSE 8080

# Define the command to run your application
CMD ["java", "-jar", "target/dataSearchService.jar"]
