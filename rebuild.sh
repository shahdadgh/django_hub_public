#!/bin/bash

# Stop all containers related to the docker-compose.yml file in the current directory
docker-compose down

# Remove all stopped containers
docker container prune -f

# Remove all networks not used by at least one container
docker network prune -f

# Remove all volumes not used by at least one container
docker volume prune -f

# Remove all dangling images
docker image prune -a -f

docker system prune -a -f

# Build the containers anew and start them
# docker-compose up --build
