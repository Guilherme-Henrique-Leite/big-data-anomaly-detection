FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    git \
    default-jdk \
    wget \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PATH=$PATH:$JAVA_HOME/bin

ENV HADOOP_VERSION=3.3.6
ENV HADOOP_HOME=/opt/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV LD_LIBRARY_PATH=$HADOOP_HOME/lib/native:$LD_LIBRARY_PATH

RUN wget https://downloads.apache.org/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz && \
    tar -xzf hadoop-${HADOOP_VERSION}.tar.gz && \
    mv hadoop-${HADOOP_VERSION} ${HADOOP_HOME} && \
    rm hadoop-${HADOOP_VERSION}.tar.gz

ENV HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"
ENV HADOOP_HOME_WARN_SUPPRESS=true
ENV HADOOP_ROOT_LOGGER=ERROR,console

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.in-project true