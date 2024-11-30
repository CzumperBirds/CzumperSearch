"""Utility functions for managing Kafka topics"""

from contextlib import closing
from kafka.admin import KafkaAdminClient, NewTopic


def does_topic_exist(topic_name: str, bootstrap_servers: str) -> bool:
    """Check if a topic exists in the Kafka cluster"""
    with closing(KafkaAdminClient(bootstrap_servers=bootstrap_servers)) as admin_client:
        topic_list = admin_client.list_topics()
    return topic_name in topic_list


def create_topic(topic_name: str, bootstrap_servers: str) -> None:
    """Create a topic in the Kafka cluster"""
    with closing(KafkaAdminClient(bootstrap_servers=bootstrap_servers)) as admin_client:
        topic = NewTopic(name=topic_name, num_partitions=1, replication_factor=1)
        admin_client.create_topics(new_topics=[topic], validate_only=False)
    print(f"Topic {topic_name} created.")
