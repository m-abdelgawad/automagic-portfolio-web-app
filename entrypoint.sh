#!/bin/sh

# Source the .env file to load environment variables
if [[ -f .env ]]; then
    source .env
fi

# Wait for database to start listening at port 5432
while ! nc -z $DB_HOSTNAME $DB_PORT; do
    echo "Database is not running yet. Will wait for 1 second."
    sleep 1
done

echo "Migrating database..."
python manage.py migrate

# Collect static
python manage.py collectstatic --noinput

# Export Google SA Key File
mkdir -p /website/cooler_jazzmin/helpers/google_analytics/data/input/
echo $GOOGLE_SA > /website/cooler_jazzmin/helpers/google_analytics/data/input/google_analytics_service-account-key.json

echo "Start running the application..."
gunicorn --access-logfile - --workers 3 --bind 0.0.0.0:8000 automagic_developer.wsgi:application
