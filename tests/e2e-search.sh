#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Define colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No color

error_handler() {
  echo -e "${RED}An error occurred at line $1 while executing: $2${NC}"
  exit 1
}

trap 'error_handler ${LINENO} "$BASH_COMMAND"' ERR

echo -e "${GREEN}Starting end-to-end tests...${NC}"

# Step 1: Run backend tests
echo -e "${GREEN}[1/3] Putting data in Kafka topic...${NC}"
python3 utils/put_data.py

# Optional wait for Kafka processing
sleep 5

# Step 2: Run frontend tests
echo -e "${GREEN}[2/3] Running Cypress frontend tests...${NC}"
cd frontend
npx cypress run
echo "Cypress exit code: $?"
cd ..


## Step 3: Clean up Elasticsearch database
#echo -e "${GREEN}[3/3] Cleaning up Elasticsearch database...${NC}"
#python3 utils/remove_data.py

# All tests passed
echo -e "${GREEN}All tests passed successfully!${NC}"