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
COPY . /app

COPY wait-for-elasticsearch.sh /app/wait-for-elasticsearch.sh

# Optionally run Maven commands to build the project
RUN mvn clean package

#RUN chmod +x /app/wait-for-elasticsearch.sh
#ENTRYPOINT ["wait-for-elasticsearch.sh"]

EXPOSE 8080

# Define the command to run your application
CMD ["java", "-jar", "target/dataSearchService.jar"]
