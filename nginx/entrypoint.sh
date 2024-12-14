#!/bin/bash

set -e

CERT_DEST="/etc/nginx/certs"
DOMAIN="automagicdeveloper.com"
SUBDOMAIN="www.automagicdeveloper.com"

# Function to obtain certificates
obtain_certificates() {
    echo "Obtaining new SSL certificates..."
    # Stop Nginx to free port 80 for Certbot
    echo "Stopping Nginx to free port 80 for Certbot..."
    nginx -s stop || true
    # Run Certbot standalone with custom paths
    certbot certonly --standalone --preferred-challenges http \
        --non-interactive --agree-tos --email muhammadabdelgawwad@gmail.com \
        --cert-path ${CERT_DEST}/fullchain.pem --key-path ${CERT_DEST}/privkey.pem \
        -d ${DOMAIN} -d ${SUBDOMAIN}
}

# Function to renew certificates
renew_certificates() {
    echo "Checking and renewing SSL certificates if needed..."
    certbot renew --quiet \
        --cert-path ${CERT_DEST}/fullchain.pem --key-path ${CERT_DEST}/privkey.pem
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
