#FROM ros:melodic-ros-core-bionic
FROM osrf/ros:melodic-desktop-full

ENV DEBIAN_FRONTEND noninteractive

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

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
# ROS setup
#
ENV ROS_DISTRO melodic

#RUN apt-get update \
#    && apt-get install -y --no-install-recommends ros-melodic-desktop-full \
#    && rm -rf /var/lib/apt/lists/*
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    sqlite3 \
    ffmpeg \
    #catkin \
    python-catkin-pkg \
    python-pymodbus \
    python-rosdistro \
    python-rospkg \
    python-rosdep-modules \
    python-rosinstall \
    python-rosinstall-generator \
    python-wstool \
    ros-melodic-moveit \
    ros-melodic-ros-control \
    ros-melodic-ros-controllers \
    ros-melodic-tf2-web-republisher \
    ros-melodic-rosbridge-server \
    ros-melodic-joint-state-publisher-gui \
    ros-melodic-joystick-drivers \
    && rm -rf /var/lib/apt/lists/*

#
# Niryo ROS stack
#
WORKDIR /catkin_ws

RUN curl -SL https://github.com/NiryoRobotics/ned_ros/archive/refs/tags/v4.0.1.tar.gz | tar -xz \
    && mv ned_ros-4.0.1 src
RUN ["bash", "-c", ". /opt/ros/melodic/setup.bash && catkin_make"]

#
# For user applications
#
RUN apt-get update && apt-get install -y python-pip \
    && rm -rf /var/lib/apt/lists/* \
    && pip install -U setuptools \
    && pip install readchar

# setup entrypoint
COPY ./ros_entrypoint.sh /
ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]
