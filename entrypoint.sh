#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Source environment variables from .env file if it exists
if [ -f .env ]; then
  echo "Sourcing .env file"
  export $(grep -v '^#' .env | xargs)
fi

# Run Django migrations to apply any database changes
echo "Running migrations..."
python manage.py migrate

# Collect static files for the Django application
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start the Gunicorn server to serve the Django application
echo "Starting Gunicorn..."
exec gunicorn --access-logfile - --workers 3 --bind 0.0.0.0:8000 automagic_developer.wsgi:application
