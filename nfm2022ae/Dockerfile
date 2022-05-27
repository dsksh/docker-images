FROM python:3.7.13-bullseye

ENV DEBIAN_FRONTEND noninteractive

RUN sed -i 's@deb.debian.org@ftp.jaist.ac.jp@g' /etc/apt/sources.list

RUN apt-get update && apt-get install -y --no-install-recommends \
    z3 \
    libz3-4 \
    libz3-dev \
    python3-pkg-resources \
    python3-z3 \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONPATH "${PYTHONPATH}:/usr/lib/python3/dist-packages"

RUN curl -sSL https://github.com/CVC4/CVC4/releases/download/1.8/cvc4-1.8-x86_64-linux-opt -o /usr/local/bin/cvc4 \
    && chmod 755 /usr/local/bin/cvc4

RUN curl -sSLO https://zenodo.org/record/6387089/files/nfm2022ae.zip \
    && unzip nfm2022ae.zip \
    && rm -f nfm2022ae.zip \
    && cd nfm2022ae/pysmt \
    && python setup.py develop 

WORKDIR /nfm2022ae
CMD ["bash"]
