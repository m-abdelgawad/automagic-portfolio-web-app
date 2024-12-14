# Use the official Python 3.10 base image
FROM python:3.10

# Install system dependencies
RUN apt-get update && \
    apt-get install -y netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

# Create a system user for running the application
RUN useradd --system --create-home --shell=/bin/bash --uid=1000 appuser

# Set the working directory inside the container
WORKDIR /website

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Change ownership of the work directory to the app user
RUN chown -R appuser:appuser /website

# Switch to the non-root user for security
USER appuser

# Ensure Python outputs logs unbuffered
ENV PYTHONUNBUFFERED=1

# Expose the application port
EXPOSE 8000

# Set the entrypoint to the custom script
ENTRYPOINT ["bash", "entrypoint.sh"]
