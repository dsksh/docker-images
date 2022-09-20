FROM openjdk:17-jdk-slim-bullseye
RUN sed -i 's@deb.debian.org@ftp.jaist.ac.jp@g' /etc/apt/sources.list
RUN apt-get update && apt-get install -y --no-install-recommends \
    libx11-6 libxext6 libxrender1 libxtst6 libxi6 \
    libfreetype6 libfontconfig1 \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /work