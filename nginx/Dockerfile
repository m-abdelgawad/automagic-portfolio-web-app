# Use the official Nginx base image
FROM nginx:latest

# Install Certbot and cron for SSL certificate management and renewal
RUN apt-get update && \
    apt-get install -y certbot cron && \
    rm -rf /var/lib/apt/lists/*

# Create the Certbot webroot directory for HTTP-01 challenges
RUN mkdir -p /var/www/certbot && \
    chown -R www-data:www-data /var/www/certbot

# Copy the Nginx configuration file into the container
COPY default.conf /etc/nginx/conf.d/default.conf

# Copy the entrypoint script into the container
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh  # Make the entrypoint script executable

# Add the renewal cron job to run every 12 hours
RUN echo "0 */12 * * * /usr/bin/certbot renew --quiet && \
    cp -L /etc/letsencrypt/live/automagicdeveloper.com/fullchain.pem /etc/nginx/certs/fullchain.pem && \
    cp -L /etc/letsencrypt/live/automagicdeveloper.com/privkey.pem /etc/nginx/certs/privkey.pem && \
    nginx -s reload" > /etc/cron.d/certbot-renew

# Set permissions for the cron job file
RUN chmod 0644 /etc/cron.d/certbot-renew

# Apply the cron job by adding it to the root user's crontab
RUN crontab /etc/cron.d/certbot-renew

# Set the entrypoint to the custom script
ENTRYPOINT ["/entrypoint.sh"]