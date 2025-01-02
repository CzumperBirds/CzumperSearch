#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Define colors for output
GREEN='\033[0;32m'
NC='\033[0m' # No color

echo -e "${GREEN}Starting end-to-end tests...${NC}"

# Step 1: Run backend tests
echo -e "${GREEN}[2/4] Putting data in kafka topic...${NC}"
python3 utils/put_data.py

sleep 5

# Step 2: Run frontend tests
echo -e "${GREEN}[3/4] Running Cypress frontend tests...${NC}"
cd frontend
npx cypress run --spec "tests/cypress/test_search.ts"
cd ..

# Step 3: Clean up Docker containers
echo -e "${GREEN}[3/4] Clean up Elasticsearch database...${NC}"
python3 utils/remove_data.py

# Step 4: Clean up Docker containers
echo -e "${GREEN}[4/4] Cleaning up Docker containers...${NC}"
docker compose down

# All tests passed
echo -e "${GREEN}All tests passed successfully!${NC}"