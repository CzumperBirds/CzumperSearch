#!/bin/bash

COMPOSE_DIRECTORIES=(
    "../data_processor"
    "../data_storage"
    "../data_search"
)

cleanup_docker_resources() {
    echo "Stopping all running Docker containers..."
    docker stop $(docker ps -aq) 2>/dev/null || echo "No containers running."

    echo "Removing all Docker containers..."
    docker rm $(docker ps -aq) 2>/dev/null || echo "No containers to remove."

    echo "Removing all Docker images..."
    docker rmi $(docker images -q) -f 2>/dev/null || echo "No images to remove."

    echo "Removing all unused volumes..."
    docker volume prune -f || echo "No volumes to prune."

    echo "All Docker resources have been cleaned."
}

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


cleanup_docker_resources

run_docker_compose "../infrastructure"

./wait-for-elasticsearch.sh

for dir in "${COMPOSE_DIRECTORIES[@]}"; do
    run_docker_compose "$dir"
done

echo "All Docker Compose services have been started."

sleep 10

