#!/bin/bash

# Exit immediately if any command exits with a non-zero status
set -e

# Check if a .env file exists and source it to load environment variables
if [ -f .env ]; then
  echo "Sourcing .env file"
  # Export all environment variables from the .env file, ignoring commented lines
  export $(grep -v '^#' .env | xargs)
fi

# Run database migrations to apply any changes to the database schema
echo "Running migrations..."
python manage.py migrate

# Collect static files into the designated static root directory
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start the Gunicorn server to serve the Django application
echo "Starting Gunicorn..."
# Execute Gunicorn with specified parameters:
# - access-logfile - : Log access logs to stdout
# - workers 3 : Number of worker processes
# - bind 0.0.0.0:8000 : Bind Gunicorn to all network interfaces on port 8000
# - automagic_developer.wsgi:application : WSGI application entry point
exec gunicorn --access-logfile - --workers 3 --bind 0.0.0.0:8000 automagic_developer.wsgi:application
