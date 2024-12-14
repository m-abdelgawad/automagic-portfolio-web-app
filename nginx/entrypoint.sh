#!/bin/sh

# Function to obtain SSL certificates
obtain_certificates() {
    certbot --nginx --non-interactive --agree-tos --email muhammadabdelgawwad@gmail.com \
        -d automagicdeveloper.com -d www.automagicdeveloper.com
}

# Check if SSL certificates exist
if [ ! -f /etc/letsencrypt/live/automagicdeveloper.com/fullchain.pem ]; then
    echo "SSL certificates not found. Obtaining certificates..."
    obtain_certificates
else
    echo "SSL certificates already exist."
fi

# Set up a cron job for certificate renewal every 12 hours
echo "0 */12 * * * certbot renew --quiet --renew-hook 'nginx -s reload'" > /etc/crontab

# Start cron in the background
cron

# Start Nginx
nginx -g 'daemon off;'