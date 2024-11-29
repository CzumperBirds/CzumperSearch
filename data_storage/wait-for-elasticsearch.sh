#!/bin/bash
set -e

echo "Waiting for Elasticsearch to be ready..."

while ! curl -s http://elasticsearch:9200 >/dev/null; do
    echo "Elasticsearch is not ready yet. Retrying in 5 seconds..."
    sleep 5
done

echo "Elasticsearch is ready. Starting..."
exec "$@"
11