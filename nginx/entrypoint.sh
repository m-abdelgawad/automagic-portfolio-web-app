#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status

# Define paths for SSL certificates
CERT_DEST="/etc/nginx/certs"
DOMAIN="automagicdeveloper.com"
SUBDOMAIN="www.automagicdeveloper.com"

# Function to obtain new SSL certificates using Certbot's standalone mode
obtain_certificates() {
    echo "Obtaining new SSL certificates..."

    # Stop Nginx to free up port 80 for Certbot
    echo "Stopping Nginx to free port 80 for Certbot..."
    nginx -s stop || true  # Ignore errors if Nginx is not running

    # Run Certbot to obtain certificates
    certbot certonly --standalone --preferred-challenges http \
        --non-interactive --agree-tos --email muhammadabdelgawwad@gmail.com \
        --cert-path ${CERT_DEST}/fullchain.pem --key-path ${CERT_DEST}/privkey.pem \
        -d ${DOMAIN} -d ${SUBDOMAIN}

    echo "SSL certificates obtained successfully."
}

# Function to renew existing SSL certificates if needed
renew_certificates() {
    echo "Checking and renewing SSL certificates if needed..."

    # Renew certificates silently
    certbot renew --quiet

    # Copy renewed certificates to CERT_DEST
    cp -L /etc/letsencrypt/live/${DOMAIN}/fullchain.pem ${CERT_DEST}/fullchain.pem
    cp -L /etc/letsencrypt/live/${DOMAIN}/privkey.pem ${CERT_DEST}/privkey.pem

    echo "SSL certificates renewed successfully."
}

# Check if SSL certificates exist; if not, obtain them
if [ ! -f "${CERT_DEST}/fullchain.pem" ] || [ ! -f "${CERT_DEST}/privkey.pem" ]; then
    obtain_certificates
else
    echo "SSL certificates found."
    renew_certificates
fi

# Start Nginx in the foreground to keep the container running
echo "Starting Nginx with SSL configuration..."
nginx -g "daemon off;"
