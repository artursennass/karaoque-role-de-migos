# Python base image
FROM python:3.10.7-slim-bullseye

# System setup
RUN apt-get update \
  && apt-get dist-upgrade -y \
  && apt-get install -y --no-install-recommends \
    git \
    ssh-client \
    software-properties-common \
    make \
    build-essential \
    ca-certificates \
    libpq-dev \
  && apt-get clean \
  && rm -rf \
    /var/lib/apt/lists/* \
    /tmp/* \
    /var/tmp/*

# Env vars
ENV PYTHONIOENCODING=utf-8
ENV LANG=C.UTF-8

# Copy requirements.txt file with dependencies
COPY requirements.txt /

# Installing dependencies with no-cache
RUN pip install --no-cache-dir -r /requirements.txt

# Copy source backend code into the image
# COPY soruce_folder/ /target_folder

# Define work directoty
# WORKDIR /app_folder

# Run your app
# CMD ["python3","app.y"]