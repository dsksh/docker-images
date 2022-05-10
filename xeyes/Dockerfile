FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN sed -i.org -e 's|ports.ubuntu.com|ftp.jaist.ac.jp/pub/Linux|g' /etc/apt/sources.list \
    && apt-get update && apt-get install -y \
       x11-apps \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

CMD ["xeyes"]
