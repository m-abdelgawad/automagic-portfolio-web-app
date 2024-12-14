# nginx/Dockerfile

FROM nginx:latest

# Install Certbot, the Nginx plugin, and Cron
RUN apt-get update && \
    apt-get install -y certbot python3-certbot-nginx cron && \
    rm -rf /var/lib/apt/lists/*

# Copy the Nginx configuration
COPY default.conf /etc/nginx/conf.d/default.conf

# Copy the entrypoint script
COPY entrypoint.sh /entrypoint.sh

# Ensure the entrypoint script is executable
RUN chmod +x /entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/entrypoint.sh"]
