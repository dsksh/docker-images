FROM osrf/ros:melodic-desktop-full

ENV DEBIAN_FRONTEND noninteractive

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

ENV ROS_DISTRO melodic

RUN sed -i 's@archive.ubuntu.com@ftp.jaist.ac.jp/pub/Linux@g' /etc/apt/sources.list

#
# NVIDIA GPU
#
RUN apt-get update && apt-get install -y --no-install-recommends \
    pkg-config \
    libxau-dev \
    libxdmcp-dev \
    libxcb1-dev \
    libxext-dev \
    libx11-dev \
    && rm -rf /var/lib/apt/lists/*

ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,graphics,utility,display

#
# Utils
#
RUN apt-get update && apt-get install -y --no-install-recommends \
    usbutils \
    curl \
    openssl \
    ca-certificates \
    gnupg \
    unzip \
    software-properties-common \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

#
# Azure Kinect
#
RUN curl -sSL https://packages.microsoft.com/keys/microsoft.asc | apt-key add \
    && apt-add-repository https://packages.microsoft.com/ubuntu/18.04/prod
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y --no-install-recommends \
    k4a-tools \
    libk4a1.4 \
    libk4a1.4-dev \
    && rm -rf /var/lib/apt/lists/*
RUN curl -sSL https://packages.microsoft.com/ubuntu/18.04/prod/pool/main/libk/libk4abt1.1/libk4abt1.1_1.1.1_amd64.deb -o /tmp/libk4abt1.1_1.1.1_amd64.deb \
    && curl -sSL https://packages.microsoft.com/ubuntu/18.04/prod/pool/main/libk/libk4abt1.1-dev/libk4abt1.1-dev_1.1.1_amd64.deb -o /tmp/libk4abt1.1-dev_1.1.1_amd64.deb \
    && echo 'libk4abt1.1 libk4abt1.1/accepted-eula-hash string 03a13b63730639eeb6626d24fd45cf25131ee8e8e0df3f1b63f552269b176e38' | debconf-set-selections \
    && echo 'libk4abt1.1 libk4abt1.1/accept-eula select true' | debconf-set-selections \
    && dpkg -i /tmp/libk4abt1.1_1.1.1_amd64.deb \
    && dpkg -i /tmp/libk4abt1.1-dev_1.1.1_amd64.deb \
    && rm -f /tmp/libk4abt1.1_1.1.1_amd64.deb /tmp/libk4abt1.1-dev_1.1.1_amd64.deb

WORKDIR /catkin_ws

RUN mkdir -p /catkin_ws/src && cd /catkin_ws/src \
    && curl -sSOL https://github.com/microsoft/Azure_Kinect_ROS_Driver/archive/refs/heads/melodic.zip \
    && unzip melodic.zip \
    && rm -f melodic.zip
RUN ["bash", "-c", ". /opt/ros/melodic/setup.bash && catkin_make"]

# setup entrypoint
COPY ./ros_entrypoint.sh /
ENTRYPOINT ["/ros_entrypoint.sh"]
#CMD ["bash"]
CMD ["roslaunch", "azure_kinect_ros_driver", "driver_with_bodytracking.launch"]
