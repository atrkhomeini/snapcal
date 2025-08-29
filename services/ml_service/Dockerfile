# Use the same clean base image as our dev container for consistency
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3.10 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY ./app /app/

# Command to run the application with auto-reload
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]