#!/bin/bash

# A script to clean all Docker resources

echo "Stopping all running containers..."
docker stop $(docker ps -q)

echo "Removing all containers..."
docker rm $(docker ps -aq)

echo "Removing all images..."
docker rmi -f $(docker images -q)

echo "Removing all volumes..."
docker volume rm $(docker volume ls -q)

echo "Removing all networks (excluding default networks)..."
docker network rm $(docker network ls -q)

echo "Performing a system-wide cleanup..."
docker system prune -a --volumes -f

echo "Docker cleanup completed!"

