# Step 1: Start from an official NVIDIA CUDA base image for GPU compatibility.
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

# Step 2: Install essential system packages and a clean Python environment.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3.10 \
    python3-pip \
    git \
    libgl1-mesa-glx \
    libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

# Step 3: Copy our project's ML requirements file.
COPY ../services/ml_service/requirements.txt /tmp/ml-requirements.txt

# Step 4: Install our Python packages into the single, global environment.
RUN python3 -m pip install --no-cache-dir -r /tmp/ml-requirements.txt

# Step 5: Tell VS Code where to find this Python installation.
ENV PYTHON_DEFAULT_EXECUTABLE=/usr/bin/python3