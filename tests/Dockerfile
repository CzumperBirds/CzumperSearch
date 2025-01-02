# Step 1: Use an official Python image as the base image for Python dependencies
FROM python:3.9-slim as python-base

# Install system dependencies for Docker (only if you need it for docker-compose or other reasons)
RUN apt-get update && apt-get install -y \
    curl \
    docker.io \
    && rm -rf /var/lib/apt/lists/*

# Step 2: Set up Cypress in a Node.js environment
FROM node:16-alpine as node-base

# Install Cypress and its dependencies
RUN apk add --no-cache \
    libc6-compat \
    libnsl \
    libstdc++ \
    && npm install -g cypress

# Step 3: Combine Python and NodeJS environments into the final image
FROM python-base

# Install Node.js (so npm is available in the final image)
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs

# Copy Python dependencies installation file and install dependencies
COPY utils/requirements.txt /app/utils/
WORKDIR /app/utils
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the Docker image
COPY . /app/

# Install frontend (Cypress) dependencies inside the 'frontend' directory
WORKDIR /app/frontend
RUN npm install && npx cypress install

WORKDIR /app
# Expose any necessary ports
EXPOSE 8282

# Make Docker socket available for the container
VOLUME [ "/var/run/docker.sock:/var/run/docker.sock" ]

# Default command to run the shell script
CMD ["bash", "/app/e2e-search.sh"]
