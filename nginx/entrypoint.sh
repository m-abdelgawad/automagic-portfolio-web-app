#!/bin/bash

set -e

CERT_DEST="/etc/nginx/certs"

# Function to obtain certificates
obtain_certificates() {
    echo "Obtaining new SSL certificates..."
    # Stop Nginx to free port 80 for Certbot
    echo "Stopping Nginx to free port 80 for Certbot..."
    nginx -s stop || true
    # Run Certbot standalone
    certbot certonly --standalone --preferred-challenges http \
        --non-interactive --agree-tos --email muhammadabdelgawwad@gmail.com \
        -d automagicdeveloper.com -d www.automagicdeveloper.com
    # Copy certificates to CERT_DEST
    echo "Copying certificates to ${CERT_DEST}..."
    cp /etc/letsencrypt/live/automagicdeveloper.com/fullchain.pem ${CERT_DEST}/fullchain.pem
    cp /etc/letsencrypt/live/automagicdeveloper.com/privkey.pem ${CERT_DEST}/privkey.pem
}

# Function to renew certificates
renew_certificates() {
    echo "Checking and renewing SSL certificates if needed..."
    certbot renew --quiet
    # Copy renewed certificates to CERT_DEST
    cp /etc/letsencrypt/live/automagicdeveloper.com/fullchain.pem ${CERT_DEST}/fullchain.pem
    cp /etc/letsencrypt/live/automagicdeveloper.com/privkey.pem ${CERT_DEST}/privkey.pem
}

# Check and obtain certificates
if [ ! -f "${CERT_DEST}/fullchain.pem" ] || [ ! -f "${CERT_DEST}/privkey.pem" ]; then
    obtain_certificates
else
    echo "SSL certificates found."
    renew_certificates
fi

# Start Nginx in the foreground
echo "Starting Nginx with SSL configuration..."
nginx -g "daemon off;"
