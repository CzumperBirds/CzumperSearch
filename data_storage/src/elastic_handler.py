from elasticsearch import Elasticsearch
class ElasticsearchHandler:
    """Handles interactions with Elasticsearch."""
    
    def __init__(self, elasticsearch_url):
        self.es = Elasticsearch([elasticsearch_url])
        self.index_name = "kafka_messages"  
    def index_message(self, message):
        """Indexes a message into Elasticsearch."""
        document = {
            "key": message.key,
            "value": message.value,
            "partition": message.partition,
            "offset": message.offset,
        }

        response = self.es.index(index=self.index_name, document=document) #TODO add apikey or sth
        return response