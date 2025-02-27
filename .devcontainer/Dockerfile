FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.in-project true
