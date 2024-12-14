# nginx/Dockerfile

FROM nginx:latest

# Install Certbot and its Nginx plugin
RUN apt-get update && \
    apt-get install -y certbot python3-certbot-nginx && \
    rm -rf /var/lib/apt/lists/*

# Create the Certbot webroot directory
RUN mkdir -p /var/www/certbot && \
    chown -R www-data:www-data /var/www/certbot

# Copy the Nginx configuration and entrypoint script
COPY default.conf /etc/nginx/conf.d/default.conf
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/entrypoint.sh"]
