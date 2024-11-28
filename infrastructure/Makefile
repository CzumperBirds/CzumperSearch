.PHONY: help_topic topic


create_topic 	= docker exec -it kafka kafka-topics --create --topic $(1) --bootstrap-server kafka:9092 --partitions 1 --replication-factor 1
kafka_producer 	= docker exec -it kafka kafka-console-producer --broker-list kafka:9092 --topic $(1)


topic:
	@$(call create_topic,$(t))


kafka:
	@$(call kafka_producer,$(t))

list_topics:
	@docker exec -it kafka kafka-topics --list --bootstrap-server kafka:9092


help_topic:
	@echo "Usage: make topic t=your_topic_name"
	@echo "Example: make topic t=my_new_topic"

help_kafka:
	@echo "Usage: make kafka t=your_topic_name"
	@echo "Example: make kafka t=my_new_topic"