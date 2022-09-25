FROM ubuntu:20.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common \
    && add-apt-repository ppa:thentrythis/samplebrain \
    && apt-get update && apt-get install -y --no-install-recommends \
    samplebrain ttf-mscorefonts-installer \
    pulseaudio \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /work
ADD https://static.thentrythis.org/samplebrain/demo.samplebrain /work
CMD ["samplebrain"]