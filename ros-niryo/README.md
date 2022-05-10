# Niryo ROS Stack

Image available on Docker Hub: [https://hub.docker.com/r/dsksh/ros-niryo](https://hub.docker.com/r/dsksh/ros-niryo)

## Running with GUI on the host X server

```sh
$ docker run --rm -it -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v ~/.Xauthority:/.Xauthority -e XAUTHORITY="/.Xauthority" ros-niryo
```

<!-- EOF -->
