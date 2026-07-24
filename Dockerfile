# Build image with (-t -> tag):
# docker build -t ml-pid-tuning .

# Run container with (--rm -> delete container after program finishes):
# docker run --rm ml-pid-tuning

# Use a lightweight image with Python 3.14
FROM python:3.14-slim

# Set the working directory inside the container
WORKDIR /app

# Copy main.py from the host into /app inside the image
COPY main.py .

# Define the default command executed when the container starts
# Equivalent to running: python main.py
CMD ["python", "main.py"]