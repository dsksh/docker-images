#FROM ros:melodic-ros-core-bionic
FROM osrf/ros:melodic-desktop-full

ENV DEBIAN_FRONTEND noninteractive

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

ENV ROS_DISTRO melodic

RUN sed -i 's@archive.ubuntu.com@ftp.jaist.ac.jp/pub/Linux@g' /etc/apt/sources.list

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
    #ros-melodic-control \
    #ros-melodic-controllers \
    ros-melodic-tf2-web-republisher \
    ros-melodic-rosbridge-server \
    ros-melodic-joint-state-publisher-gui \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /catkin_ws_niryo_ned

RUN curl -SL https://github.com/NiryoRobotics/ned_ros/archive/refs/tags/v4.0.1.tar.gz | tar -xz \
    && mv ned_ros-4.0.1 src
RUN ["bash", "-c", ". /opt/ros/melodic/setup.bash && catkin_make"]

# setup entrypoint
COPY ./ros_entrypoint.sh /
ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]
