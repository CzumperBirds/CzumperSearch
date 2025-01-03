import os
from elasticsearch import Elasticsearch
from requests.exceptions import RequestException

def delete_data_from_es():
    # Read Elasticsearch connection details from environment variable
    es_host = os.getenv('ELASTICSEARCH_HOST', 'elasticsearch')
    es_port = os.getenv('ELASTICSEARCH_PORT', 9200)
    es_username = os.getenv('ELASTIC_USERNAME', 'elastic')
    es_password = os.getenv('ELASTIC_PASSWORD', '')

    # Connect to Elasticsearch instance using environment variables
    es = Elasticsearch(
        [f'http://{es_host}:{es_port}'],
        http_auth=(es_username, es_password)
    )

    # Index name to delete the data from
    index_name = 'processed-resources'

    try:
        # Check if the index exists before attempting deletion
        if es.indices.exists(index=index_name):
            # Deleting the index
            es.indices.delete(index=index_name)
            print(f"Index '{index_name}' and all its data have been deleted.")
        else:
            print(f"Index '{index_name}' does not exist.")
    except RequestException as e:
        print(f"Error connecting to Elasticsearch: {str(e)}")

if __name__ == "__main__":
    delete_data_from_es()