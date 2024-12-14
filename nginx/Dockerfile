FROM nginx:latest

# Install Certbot and cron
RUN apt-get update && apt-get install -y certbot cron && \
    rm -rf /var/lib/apt/lists/*

# Add the renewal cron job
RUN echo "0 */12 * * * certbot renew --quiet && cp -L /etc/letsencrypt/live/automagicdeveloper.com/fullchain.pem /etc/nginx/certs/fullchain.pem && cp -L /etc/letsencrypt/live/automagicdeveloper.com/privkey.pem /etc/nginx/certs/privkey.pem && nginx -s reload" > /etc/cron.d/certbot-renew
RUN chmod 0644 /etc/cron.d/certbot-renew && crontab /etc/cron.d/certbot-renew

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Start Nginx and cron
CMD ["/entrypoint.sh"]
