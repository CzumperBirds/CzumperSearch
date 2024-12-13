FROM maven:3.9.9-eclipse-temurin-23 AS build

WORKDIR /app

COPY pom.xml .
COPY src ./src

RUN mvn clean package -DskipTests
RUN mvn wrapper:wrapper

FROM openjdk:23-jdk-slim

WORKDIR /app

COPY --from=build /app/target/data_processor_service-0.0.1-SNAPSHOT.jar app.jar

ENTRYPOINT ["java", "-jar", "app.jar"]
