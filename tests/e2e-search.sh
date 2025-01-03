#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Define colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No color

error_handler() {
  echo -e "${RED}An error occurred in the script execution. Exiting...${NC}"
  exit 1
}

trap error_handler ERR

echo -e "${GREEN}Starting end-to-end tests...${NC}"

# Step 1: Run backend tests
echo -e "${GREEN}[1/4] Putting data in Kafka topic...${NC}"
python3 utils/put_data.py

# Optional wait for Kafka processing
sleep 5

# Step 2: Run frontend tests
echo -e "${GREEN}[2/4] Running Cypress frontend tests...${NC}"
cd frontend
npx cypress run || exit 1 # Ensure explicit handling
cd ..

# Step 3: Clean up Elasticsearch database
echo -e "${GREEN}[3/4] Cleaning up Elasticsearch database...${NC}"
python3 utils/remove_data.py || exit 1 # Ensure explicit handling

# Step 4: (Optional) Clean up Docker containers
# Uncomment the section if needed
# echo -e "${GREEN}[4/4] Cleaning up Docker containers...${NC}"
# docker compose down || exit 1 # Ensure explicit handling

# All tests passed
echo -e "${GREEN}All tests passed successfully!${NC}"