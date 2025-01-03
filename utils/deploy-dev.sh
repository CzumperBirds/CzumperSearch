#!/bin/bash

COMPOSE_DIRECTORIES=(
    "../data_processor"
    "../data_storage"
    "../data_search"
    "../frontend/CzumperSearch"
)

# Function to run docker-compose in a given directory
run_docker_compose() {
    local dir=$1
    echo "Starting Docker Compose in: $dir"

    # Navigate to the directory
    cd "$dir" || { echo "Failed to navigate to $dir"; exit 1; }

    # Run docker-compose up
    docker-compose -f docker-compose.dev.yml build
    docker-compose -f docker-compose.dev.yml up -d
    if [ $? -ne 0 ]; then
        echo "Failed to start services in: $dir"
        exit 1
    else
        echo "Services started successfully in: $dir"
    fi
}

run_docker_compose "../infrastructure"

/bin/bash wait-for-elasticsearch.sh

for dir in "${COMPOSE_DIRECTORIES[@]}"; do
    run_docker_compose "$dir"
done

echo "All Docker Compose services have been started."
