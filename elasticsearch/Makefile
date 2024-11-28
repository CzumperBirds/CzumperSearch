.PHONY: up

up:
	@docker-compose up -d

down:
	@docker-compose down -v --remove-orphans

logs:
	@docker-compose logs -f

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  up        Start the Elasticsearch cluster"
	@echo "  down      Stop the Elasticsearch cluster + rm vol"
	@echo "  logs      Show the logs of the Elasticsearch cluster"
	@echo "  help      Show this help message"