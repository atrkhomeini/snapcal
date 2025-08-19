# Start from an official Python 3.10 image.
FROM mcr.microsoft.com/devcontainers/python:3.10

# [Optional] Add any OS-level packages you might need.
# For example, to install Git.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends git

# [Optional] You can install a global version of pylint or other tools here
# RUN pip install pylint

# [Done] The rest of your project's dependencies (FastAPI, PyTorch, etc.)
# will be installed by the docker-compose.yml file.