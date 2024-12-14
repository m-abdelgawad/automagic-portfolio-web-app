# nginx/Dockerfile

# Use the official Nginx base image from Docker Hub
FROM nginx:latest

# Update the package list to ensure we have the latest information
RUN apt-get update

# Install Certbot and cron for SSL certificate management and scheduling renewals
RUN apt-get install -y certbot cron

# Clean up the package lists to reduce the image size
RUN rm -rf /var/lib/apt/lists/*

# Create the Certbot webroot directory to serve challenge files for domain verification
RUN mkdir -p /var/www/certbot

# Change ownership of the Certbot webroot directory to the 'www-data' user and group used by Nginx
RUN chown -R www-data:www-data /var/www/certbot

# Copy the custom Nginx configuration file into the container
COPY default.conf /etc/nginx/conf.d/default.conf

# Copy the custom entrypoint script into the container
COPY entrypoint.sh /entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /entrypoint.sh

# Add the Certbot renewal cron job to run every 12 hours
RUN echo "0 */12 * * * /usr/bin/certbot renew --quiet && cp -L /etc/letsencrypt/live/automagicdeveloper.com/fullchain.pem /etc/nginx/certs/fullchain.pem && cp -L /etc/letsencrypt/live/automagicdeveloper.com/privkey.pem /etc/nginx/certs/privkey.pem && nginx -s reload" > /etc/cron.d/certbot-renew

# Set the appropriate permissions for the cron job file
RUN chmod 0644 /etc/cron.d/certbot-renew

# Apply the cron job by adding it to the cron daemon's crontab
RUN crontab /etc/cron.d/certbot-renew

# Define the default command to run when the container starts, which is the entrypoint script
CMD ["/entrypoint.sh"]
