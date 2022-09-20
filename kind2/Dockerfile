#FROM ocaml/opam:alpine-ocaml-4.14-flambda as builder
FROM ocaml/opam:debian-11-ocaml-4.14-flambda as builder

USER root

#RUN apk add make m4 g++ musl-dev git \
#    zeromq-dev libzmq-static libsodium-static

RUN sed -i 's@deb.debian.org/debian @ftp.jaist.ac.jp/debian @g' /etc/apt/sources.list
RUN apt-get update && apt-get install -y --no-install-recommends \
    make m4 g++ musl-dev git \
    libzmq3-dev libsodium-dev \
    wget pkg-config && \
    rm -rf /var/lib/apt/lists/* 

USER opam

#COPY --chown=opam:opam . kind2-build/

# Build Kind 2
WORKDIR kind2-build

RUN wget -qq https://github.com/kind2-mc/kind2/archive/refs/tags/v1.6.0.tar.gz && \
    tar xvzf v1.6.0.tar.gz && \
    mv kind2-1.6.0/* .

# Note: we use remote OPAM repo until local one is updated
RUN eval $(opam env) && \
    opam repo set-url default https://opam.ocaml.org && \
    opam update && opam install -y . --deps-only && \
    #make static && \
    make build && \
    strip bin/kind2

#FROM alpine:latest
FROM debian:bullseye-slim

USER root

RUN sed -i 's@deb.debian.org/debian @ftp.jaist.ac.jp/debian @g' /etc/apt/sources.list
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget bash \
    musl libzmq5 libsodium23 \
    z3 && \
    rm -rf /var/lib/apt/lists/* 

## Retrieve Yices 2
RUN wget --no-check-certificate -qq https://yices.csl.sri.com/releases/2.6.2/yices-2.6.2-x86_64-pc-linux-gnu-static-gmp.tar.gz \
    && tar xvf yices-2.6.2-x86_64-pc-linux-gnu-static-gmp.tar.gz \
    && cp ./yices-2.6.2/bin/yices-smt2 /usr/local/bin/ \
    && rm -rf yices-* \
    && echo Success || true

## Retrieve JKind and cvc5 (required for certification)
#RUN wget -qq https://github.com/loonwerks/jkind/releases/download/v4.4.2/jkind-4.4.2.zip && unzip jkind-4.4.2.zip \
# && cp ./jkind/jkind ./jkind/*.jar /bin/ \
# && rm -rf jkind* \
# && wget -qq https://github.com/cvc5/cvc5/releases/latest/download/cvc5-Linux -O cvc5 \
# && mv cvc5 /bin/ \
# && chmod a+x /bin/cvc5 \
# && echo Success || true

RUN wget --no-check-certificate -qq https://github.com/cvc5/cvc5/releases/latest/download/cvc5-Linux -O cvc5 \
    && mv cvc5 /usr/local/bin/ \
    && chmod a+x /usr/local/bin/cvc5 \
    && echo Success || true

## Install Z3 and Java (required by JKind)
#RUN apk add z3 openjdk11 && adduser --disabled-password --gecos KIND2 kind2

RUN adduser --disabled-password --gecos KIND2 kind2

COPY --chown=kind2:kind2 --from=builder /home/opam/kind2-build/bin/kind2 /usr/local/bin/

USER kind2
WORKDIR work
ENTRYPOINT ["kind2"]
#CMD ["kind2"]