#!/bin/bash

# Function to handle errors
error_handler() {
    echo "An error occurred on line $1"
    exit 1
}

# Set trap for error handling
trap 'error_handler $LINENO' ERR

echo "Starting deployment..."

sleep 200

# Simulate some deployment steps
# Uncomment the following line to simulate an error
# false  # Simulate a failure

echo "Deployment to production is successful!"
