# Use the official PyTorch image with CUDA 12.1 support
FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-runtime

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first for layer caching
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application source code
COPY ./app /app/

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]