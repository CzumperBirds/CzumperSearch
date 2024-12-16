.PHONY: build, up, down

build:
	@docker compose build


up:
	@docker compose up


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