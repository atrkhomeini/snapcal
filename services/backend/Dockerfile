# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# --- Layer Caching for Faster Builds ---
# Copy the requirements file first. Docker will cache this layer.
# If requirements.txt doesn't change, Docker won't re-install packages on subsequent builds.
COPY requirements.txt .

# Install any needed system packages
# RUN apt-get update && apt-get install -y ...

# Install the Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# --- Application Code ---
# Copy the rest of the application source code into the container
COPY ./app /app/

# Command to run the application
# This tells uvicorn to run the 'app' instance from the main.py file.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]