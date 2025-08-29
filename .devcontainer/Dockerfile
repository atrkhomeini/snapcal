# Use the official PyTorch image with CUDA 12.1 support
FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-runtime

# [Optional] Add any OS-level packages you might need.
# For example, to install Git.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends git

# [Optional] You can install a global version of pylint or other tools here
# RUN pip install pylint
# --- ADD THESE LINES AT THE END ---

# Copy the ML service's requirements file into the container
COPY ../services/ml_service/requirements.txt /tmp/ml-requirements.txt

# Install the ML dependencies into our development environment
RUN pip install --no-cache-dir -r /tmp/ml-requirements.txt

# [Done] The rest of your project's dependencies (FastAPI, PyTorch, etc.)
# will be installed by the docker-compose.yml file.