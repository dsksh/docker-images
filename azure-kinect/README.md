# Azure Kinect on Ubuntu 18.04

## Environment

- Host OS: Ubuntu 20.04
- Graphics card: GeForce RTX 2080 Ti
- NVIDIA driver version: 470.103.01
    - [Does not work w/ later versions.](https://github.com/microsoft/Azure-Kinect-Sensor-SDK/issues/1696)
- CUDA version: 11.4

## Usage

1. Setup the udev rule on the host:
   ```sh
   $ sudo curl https://github.com/microsoft/Azure-Kinect-Sensor-SDK/raw/develop/scripts/99-k4a.rules -o /etc/udev/rules.d/99-k4a.rules
   ```
2. Detach and reattach the Azure Kinect device.
3. Execute a Docker container:
   ```sh
   $ docker run --privileged --runtime=nvidia -rm -it -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix dsksh/azure-kinect
   ```
4. Execute an app e.g. `k4aviewer` and `k4abt_simple_3d_viewer`.

## Reference

- [Linux Software Repository for Microsoft Products](https://docs.microsoft.com/en-us/windows-server/administration/linux-package-repository-for-microsoft-software)
- [Azure Kinect on Ubuntu 18.04](https://gist.github.com/madelinegannon/c212dbf24fc42c1f36776342754d81bc)
- [Using apt to install k4a package in a non-interactive environment fails](https://github.com/microsoft/Azure-Kinect-Sensor-SDK/issues/1190)

<!-- EOF -->
