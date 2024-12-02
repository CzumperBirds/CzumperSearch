# Stage 1: Build Stage
FROM maven:3.9.9-eclipse-temurin-23 AS build

# Set the working directory inside the container
WORKDIR /app

# Copy the pom.xml and download dependencies (to cache these layers)
COPY pom.xml .
COPY src ./src

# Build the application
RUN mvn clean package -DskipTests

RUN mvn wrapper:wrapper

# Stage 2: Runtime Stage
FROM openjdk:23-jdk

# Set the working directory inside the container
WORKDIR /app

# Copy the JAR file from the build stage
COPY --from=build /app/target/data_processor_service-0.0.1-SNAPSHOT.jar app.jar

# Command to run the application
ENTRYPOINT ["java", "-jar", "app.jar"]
