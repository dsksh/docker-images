FROM ubuntu:18.04

RUN sed -i 's@archive.ubuntu.com@ftp.jaist.ac.jp/pub/Linux@g' /etc/apt/sources.list

##############################################################################
##                          for using nvidia gpu                            ##
##############################################################################
RUN apt-get update && apt-get install -y --no-install-recommends \
    pkg-config \
    libxau-dev \
    libxdmcp-dev \
    libxcb1-dev \
    libxext-dev \
    libx11-dev \
    && rm -rf /var/lib/apt/lists/*

ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES graphics

##############################################################################
##                                  common                                  ##
##############################################################################
# install ifconfig & ping
RUN apt-get update && apt-get install -y --no-install-recommends \
    usbutils \
    curl \
    openssl \
    ca-certificates \
    gnupg \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

##############################################################################
##                           azure kinect install                           ##
##############################################################################
RUN curl -SL https://packages.microsoft.com/keys/microsoft.asc | apt-key add \
    && apt-add-repository https://packages.microsoft.com/ubuntu/18.04/prod
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y --no-install-recommends \
    k4a-tools \
    libk4a1.4-dev \
    && rm -rf /var/lib/apt/lists/*

#RUN mkdir -p /etc/udev/rules.d \
#    && curl https://github.com/microsoft/Azure-Kinect-Sensor-SDK/raw/develop/scripts/99-k4a.rules -o /etc/udev/rules.d/99-k4a.rules

CMD ["bash"]
