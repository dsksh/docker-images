# Niryo ROS Stack

Image available on Docker Hub: [https://hub.docker.com/r/dsksh/ros-niryo](https://hub.docker.com/r/dsksh/ros-niryo)

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
