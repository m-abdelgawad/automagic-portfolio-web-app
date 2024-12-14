#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Define the destination directory for SSL certificates within the container
CERT_DEST="/etc/nginx/certs"

# Define the main domain and subdomain for which SSL certificates are issued
DOMAIN="automagicdeveloper.com"
SUBDOMAIN="www.automagicdeveloper.com"

# Function to obtain new SSL certificates using Certbot's standalone mode
obtain_certificates() {
    echo "Obtaining new SSL certificates..."

    # Stop Nginx to free up port 80 for Certbot to perform the HTTP-01 challenge
    echo "Stopping Nginx to free port 80 for Certbot..."
    nginx -s stop || true  # Stop Nginx gracefully, ignore errors if Nginx is not running

    # Run Certbot in standalone mode to obtain SSL certificates
    certbot certonly --standalone --preferred-challenges http \
        --non-interactive --agree-tos --email muhammadabdelgawwad@gmail.com \
        --cert-path ${CERT_DEST}/fullchain.pem --key-path ${CERT_DEST}/privkey.pem \
        -d ${DOMAIN} -d ${SUBDOMAIN}
}

# Function to renew existing SSL certificates if they are due for renewal
renew_certificates() {
    echo "Checking and renewing SSL certificates if needed..."

    # Run Certbot's renew command quietly to renew certificates that are near expiration
    certbot renew --quiet \
        --cert-path ${CERT_DEST}/fullchain.pem --key-path ${CERT_DEST}/privkey.pem
}

# Main logic to check the existence of SSL certificates and obtain or renew them accordingly
if [ ! -f "${CERT_DEST}/fullchain.pem" ] || [ ! -f "${CERT_DEST}/privkey.pem" ]; then
    # If the SSL certificate files do not exist, obtain new certificates
    obtain_certificates
else
    # If SSL certificates are found, check and renew them if necessary
    echo "SSL certificates found."
    renew_certificates
fi

# Start Nginx in the foreground with the SSL configuration
echo "Starting Nginx with SSL configuration..."
nginx -g "daemon off;"
