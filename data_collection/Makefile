# Variables
DOCKER_COMPOSE_FILE=docker-compose.dev.yml
SERVICE_URL=http://localhost:8000/api/v1/data-collection

# Targets
.PHONY: install build stop start status test

install:
	poetry shell
	poetry install

build:
	docker compose -f $(DOCKER_COMPOSE_FILE) up -d --build

stop:
	curl -X 'POST' \
	'$(SERVICE_URL)/control' \
	-H 'Content-Type: application/json' \
	-d '{"action": "stop"}'

start:
	curl -X 'POST' \
	'$(SERVICE_URL)/control' \
	-H 'Content-Type: application/json' \
	-d '{"action": "start"}'

status:
	curl -X 'GET' \
	'$(SERVICE_URL)/status'

test:
	poetry run pytest