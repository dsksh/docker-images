# Niryo ROS Stack

Image available on Docker Hub: [https://hub.docker.com/r/dsksh/ros-niryo](https://hub.docker.com/r/dsksh/ros-niryo)

[ROS](https://www.ros.org/) stack for [Niryo Ned robots](https://niryo.com/product/ned-education-research-cobot/).

Following the [official instrallation steps](https://docs.niryo.com/dev/ros/v4.1.0/en/source/installation/ubuntu_18.html) on Ubuntu 18.

## Running with GUI on the host X server

Allow root authentication on the host:
```sh
$ xhost +SI:localuser:root
```

Execute a Docker container:
```sh
$ docker run --rm -it -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix dsksh/ros-niryo
```

<!-- EOF -->
