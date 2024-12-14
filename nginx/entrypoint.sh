#!/bin/bash

set -e

# Paths for SSL certificates
CERT_DIR="/etc/letsencrypt/live/automagicdeveloper.com"
CERT_DEST="/etc/nginx/certs"

# Check if certificates exist or need renewal
check_and_obtain_certificates() {
    if [ ! -f "${CERT_DIR}/fullchain.pem" ] || [ ! -f "${CERT_DIR}/privkey.pem" ]; then
        echo "Obtaining new SSL certificates..."
        # Stop Nginx to free port 80 for Certbot
        nginx -s stop || true
        certbot certonly --standalone --preferred-challenges http \
            --non-interactive --agree-tos --email muhammadabdelgawwad@gmail.com \
            -d automagicdeveloper.com -d www.automagicdeveloper.com
    fi
}

# Sync certificates to the desired directory
sync_certificates() {
    echo "Syncing SSL certificates to ${CERT_DEST}..."
    mkdir -p ${CERT_DEST}
    cp -L ${CERT_DIR}/fullchain.pem ${CERT_DEST}/fullchain.pem
    cp -L ${CERT_DIR}/privkey.pem ${CERT_DEST}/privkey.pem
}

# Main entrypoint logic
check_and_obtain_certificates
sync_certificates

# Start cron in the background
echo "Starting cron for certificate renewal..."
cron

# Start Nginx in the foreground
echo "Starting Nginx with SSL configuration..."
nginx -g "daemon off;"
