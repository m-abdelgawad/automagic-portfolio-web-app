#!/bin/sh

set -e

# Start Nginx in HTTP-only mode
echo "Starting Nginx in HTTP-only mode..."
nginx &

# Wait for Nginx to start
sleep 5

# Obtain SSL certificates using Certbot
if [ ! -f /etc/letsencrypt/live/automagicdeveloper.com/fullchain.pem ]; then
    echo "SSL certificates not found. Obtaining certificates..."
    certbot certonly --webroot --webroot-path=/var/www/certbot \
        --non-interactive --agree-tos -m muhammadabdelgawwad@gmail.com \
        -d automagicdeveloper.com
else
    echo "SSL certificates already exist."
fi

# Reload Nginx to enable HTTPS
echo "Reloading Nginx with SSL configuration..."
nginx -s reload

# Keep Nginx running in the foreground
echo "Starting Nginx in foreground..."
nginx -g "daemon off;"
