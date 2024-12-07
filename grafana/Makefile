.PHONY: prod-delete, prod-up

prod-delete:
# -grafana prod down and remove volumes
	@docker compose -f docker-compose.prod.yml down -v --remove-orphans

prod-up:
# -grafana prod up in detached mode
	@docker compose -f docker-compose.prod.yml up -d --build

prod-upv:
# -grafana prod up in Verbose mode
	@docker compose -f docker-compose.prod.yml up --build