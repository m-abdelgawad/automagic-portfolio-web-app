# nginx/Dockerfile

FROM nginx:latest

# Install Certbot and cron
RUN apt-get update && \
    apt-get install -y certbot cron && \
    rm -rf /var/lib/apt/lists/*

# Create the Certbot webroot directory
RUN mkdir -p /var/www/certbot && \
    chown -R www-data:www-data /var/www/certbot

# Copy the Nginx configuration and entrypoint script
COPY default.conf /etc/nginx/conf.d/default.conf
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Add the renewal cron job
RUN echo "0 */12 * * * /usr/bin/certbot renew --quiet && cp -L /etc/letsencrypt/live/automagicdeveloper.com/fullchain.pem /etc/nginx/certs/fullchain.pem && cp -L /etc/letsencrypt/live/automagicdeveloper.com/privkey.pem /etc/nginx/certs/privkey.pem && nginx -s reload" > /etc/cron.d/certbot-renew

# Set permissions for the cron file
RUN chmod 0644 /etc/cron.d/certbot-renew

# Apply the cron job
RUN crontab /etc/cron.d/certbot-renew

# Start cron in the background and then start Nginx
CMD ["/entrypoint.sh"]
