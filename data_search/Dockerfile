FROM maven:3.9.9-eclipse-temurin-23 AS build

WORKDIR /app

COPY pom.xml .
COPY src ./src

RUN mvn clean package -DskipTests
RUN mvn wrapper:wrapper

FROM openjdk:23-jdk-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl

COPY --from=build /app/target/dataSearchService.jar app.jar

COPY wait-for-elasticsearch.sh .

EXPOSE 8080

ENTRYPOINT ["./wait-for-elasticsearch.sh"]

CMD ["java", "-jar", "app.jar"]
