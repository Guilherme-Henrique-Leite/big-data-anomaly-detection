FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    git \
    default-jdk \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PATH=$PATH:$JAVA_HOME/bin

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.in-project true
