.PHONY: build, up, down

build:
	@docker compose build


up:
	@docker compose up


down:
	@docker compose down -v --remove-orphans


elk_indicies:
	@curl -X GET "localhost:9200/_cat/indices?v"