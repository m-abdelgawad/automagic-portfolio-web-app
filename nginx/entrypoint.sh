#!/bin/sh

set -e

# Function to check if port 80 is responding
verify_port_80() {
    echo "Checking if port 80 is accessible..."
    for i in $(seq 1 10); do
        if curl -s http://127.0.0.1/.well-known/acme-challenge/ > /dev/null 2>&1; then
            echo "Port 80 is accessible."
            return 0
        fi
        echo "Port 80 not accessible yet. Retrying in 2 seconds... ($i/10)"
        sleep 2
    done
    echo "Failed to access port 80. Exiting."
    exit 1
}

# Start Nginx in HTTP-only mode
echo "Starting Nginx in HTTP-only mode..."
nginx &

# Wait for Nginx to start and verify port 80
sleep 5
verify_port_80

# Obtain SSL certificates using Certbot
if [ ! -f /etc/letsencrypt/live/automagicdeveloper.com/fullchain.pem ]; then
    echo "SSL certificates not found. Obtaining certificates..."
    certbot certonly --webroot --webroot-path=/var/www/certbot \
        --non-interactive --agree-tos --email muhammadabdelgawwad@gmail.com \
        -d automagicdeveloper.com -d www.automagicdeveloper.com
else
    echo "SSL certificates already exist."
fi

# Reload Nginx with SSL configuration
echo "Reloading Nginx with SSL configuration..."
nginx -s reload

# Keep Nginx running in the foreground
echo "Starting Nginx in foreground with HTTPS..."
nginx -g "daemon off;"
