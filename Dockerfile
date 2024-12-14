# app/Dockerfile

# Use the official Python 3.10 base image from Docker Hub
FROM python:3.10

# Update the package list to ensure we have the latest information
RUN apt-get update

# Install necessary dependencies, such as netcat for network operations
RUN apt-get install -y netcat-openbsd

# Create a system user 'appuser' with no password and a home directory
RUN useradd --system --create-home --shell=/bin/bash --uid=1000 appuser

# Set the working directory inside the container to /website
WORKDIR /website

# Copy only the requirements.txt file to leverage Docker layer caching
COPY requirements.txt .

# Install Python dependencies listed in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Change the ownership of the /website directory to 'appuser' to ensure proper permissions
RUN chown -R appuser:appuser /website

# Switch to the non-root user 'appuser' for running the application
USER appuser

# Ensure Python outputs logs unbuffered for real-time logging
ENV PYTHONUNBUFFERED=1

# Expose port 8000 to allow external access to the Django application
EXPOSE 8000

# Define the entrypoint script to run commands before starting the application
ENTRYPOINT ["bash", "entrypoint.sh"]
