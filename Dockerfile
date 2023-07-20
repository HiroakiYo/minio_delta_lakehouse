# Docker file for building delta lake management service

ARG BASE_CONTAINER=apache/spark-py:v3.4.0
FROM $BASE_CONTAINER as spark
FROM spark as delta

USER root
ARG DELTA_SPARK_VERSION="2.4.0"
ARG DELTALAKE_VERSION="2.4.0"

# DEBUG TOOLS
RUN apt-get update && apt-get install -y iputils-ping
RUN apt-get install -y vim

RUN pip install --quiet --no-cache-dir delta-spark==${DELTA_SPARK_VERSION}
# Spark and deltalake depdency
ARG WORKDIR=/opt/spark/work-dir
ENV DELTA_PACKAGE_VERSION=delta-core_2.12:${DELTA_SPARK_VERSION}
ADD ./minio-jar/aws-java-sdk-bundle-1.12.262.jar /opt/spark/jars
ADD ./minio-jar/hadoop-aws-3.3.4.jar /opt/spark/jars

# Flask setup
RUN pip install Flask
