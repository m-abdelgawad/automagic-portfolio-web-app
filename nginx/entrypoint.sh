# nginx/entrypoint.sh

#!/bin/sh

set -e

# Function to obtain SSL certificates using webroot method
obtain_certificates() {
    certbot certonly --webroot --non-interactive --agree-tos --email muhammadabdelgawwad@gmail.com \
        -w /var/www/certbot -d automagicdeveloper.com -d www.automagicdeveloper.com
}

# Start Nginx in the background
echo "Starting Nginx in the background..."
nginx -g "daemon off;" &

# Wait for Nginx to start
sleep 5

# Check if SSL certificates exist
if [ ! -f /etc/letsencrypt/live/automagicdeveloper.com/fullchain.pem ]; then
    echo "SSL certificates not found. Obtaining certificates..."
    obtain_certificates
else
    echo "SSL certificates already exist."
fi

# Reload Nginx to apply SSL configuration
echo "Reloading Nginx with SSL certificates..."
nginx -s reload

# Set up a cron job for certificate renewal every 12 hours
echo "Setting up cron job for certificate renewal..."
echo "0 */12 * * * certbot renew --quiet --renew-hook 'nginx -s reload'" > /etc/crontab

# Start cron in the background
echo "Starting cron daemon..."
cron

# Keep the script running to keep the container alive
echo "Entrypoint script completed. Keeping the container alive..."
tail -f /dev/null
