#!/bin/sh

set -e

# Function to obtain SSL certificates using Certbot with Nginx plugin
obtain_certificates() {
    certbot --nginx --non-interactive --agree-tos --email muhammadabdelgawwad@gmail.com \
        -d automagicdeveloper.com -d www.automagicdeveloper.com --redirect
}

# Start Nginx in HTTP-only mode
echo "Starting Nginx in HTTP-only mode..."
nginx &

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
echo "Reloading Nginx with SSL configuration..."
nginx -s reload

# Keep Nginx running in the foreground
echo "Starting Nginx in foreground with HTTPS..."
nginx -g "daemon off;"
