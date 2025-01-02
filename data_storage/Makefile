.PHONY: install, build, up, down
DOCKER_COMPOSE_FILE=docker-compose.dev.yml

up:
	docker compose -f $(DOCKER_COMPOSE_FILE) up -d --build

install:
	poetry shell
	poetry install

down:
	@docker compose down -v --remove-orphans


elk_indicies:
	@curl -X GET "localhost:9200/_cat/indices?v"

# elk_clear:
# 	@echo Clearing all data from elasticsearch for topic 'kafka_messages'
# 	@curl -X DELETE "http://localhost:9200/kafka_messages"

elk_get:
	@echo Getting all data from elasticsearch for topic 'processed-resources'
	@curl -X GET "localhost:9200/processed-resources/_search?pretty"

black:
	@black ./src