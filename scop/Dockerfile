FROM openjdk:11-jdk-slim-bullseye as builder

RUN sed -i 's@deb.debian.org/debian @ftp.jaist.ac.jp/debian @g' /etc/apt/sources.list
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash curl lzma \
    make g++ \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /work
ENV DIR "/work/scop-for-xcsp18-180731"
ENV MROOT "${DIR}/MapleCOMSPS"

COPY SolverTypes.h /work

RUN curl -sSL https://tsoh.org/sCOP/scop-for-xcsp18-180731.tar.gz | tar xz \
    && cp SolverTypes.h ${MROOT}/core \
    && cd ${MROOT}/simp \
    && make r \
    && cd ${DIR}/syrup \
    && make

#

FROM openjdk:11-jdk-slim-bullseye 

RUN sed -i 's@deb.debian.org/debian @ftp.jaist.ac.jp/debian @g' /etc/apt/sources.list
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash lzma \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /work
ENV DIR "/work/scop-for-xcsp18-180731"

RUN adduser --disabled-password --gecos sCOP scop

COPY --chown=scop:scop --from=builder ${DIR} ${DIR}

USER scop
WORKDIR work