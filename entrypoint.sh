#!/bin/bash

# Exit on error
set -e

# Source the environment variables
if [ -f .env ]; then
  echo "Sourcing .env file"
  export $(grep -v '^#' .env | xargs)
fi

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start the Gunicorn server
echo "Starting Gunicorn..."
exec gunicorn --access-logfile - --workers 3 --bind 0.0.0.0:8000 automagic_developer.wsgi:application
