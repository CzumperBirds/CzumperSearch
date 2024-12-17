from elasticsearch import Elasticsearch


class ElasticsearchHandler:
    """Handles interactions with Elasticsearch."""

    def __init__(self, elasticsearch_url, username=None, password=None):
        self.es = Elasticsearch(
            [elasticsearch_url],
            http_auth=(username, password) if username and password else None,
        )
        self.index_name = "kafka_messages"

    def index_message(self, index_name, document):
        """Indexes a document into Elasticsearch."""
        response = self.es.index(index=index_name, document=document)
        return response

    def search_all(self):
        """Searches all documents in the index."""
        response = self.es.search(
            index=self.index_name, body={"query": {"match_all": {}}}
        )
        return response
