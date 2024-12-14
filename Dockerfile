FROM python:3.10

# Install dependencies
RUN apt-get update && apt-get install -y netcat-openbsd

# Create app user
RUN useradd --system --create-home --shell=/bin/bash --uid=1000 appuser

WORKDIR /website

# Copy only the requirements file first
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Change ownership of the work directory
RUN chown -R appuser:appuser /website

# Switch to the non-root user
USER appuser

# Ensure Python outputs logs unbuffered
ENV PYTHONUNBUFFERED=1

# Expose the application port
EXPOSE 8000

# Entrypoint to run commands before starting the app
ENTRYPOINT ["bash", "entrypoint.sh"]
