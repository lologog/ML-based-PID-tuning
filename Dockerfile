# Build image with (-t -> tag):
# docker build -t ml-pid-tuning .

# Use a lightweight image with Python 3.14
FROM python:3.14-slim

# Set the working directory inside the container
WORKDIR /app

# Install required Python packages
RUN pip install pytest matplotlib

# Copy project files into the image
COPY src ./src
COPY tests ./tests

# Add src directory to Python module search path
ENV PYTHONPATH=/app/src