#!/bin/bash

# Fetch the password from Vault
VAULT_ADDR="http://127.0.0.1:8200"  # Replace with your Vault server URL
VAULT_TOKEN="hvs.NiDaD59gQXojPDhUH0g0cPoF"  # Replace with your actual Vault token
SECRET_PATH="secret/data/grafana/config"  # Vault secret path

# Use the Vault CLI or API to fetch the secret
PASSWORD=$(curl -s --header "X-Vault-Token: $VAULT_TOKEN" \
    --request GET $VAULT_ADDR/v1/$SECRET_PATH \
    | jq -r '.data.data.GF_SECURITY_ADMIN_PASSWORD')  # Extract the 'password' field

# Export the password as an environment variable
export GF_SECURITY_ADMIN_PASSWORD=$PASSWORD

echo $GF_SECURITY_ADMIN_PASSWORD
# Start Docker Compose with the environment variable
docker-compose -f docker-compose.prod.yml up

