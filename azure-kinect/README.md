# Azure Kinect on Ubuntu 18.04

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
4. Execute an app e.g. `k4aviewer`.

## Reference

- [Linux Software Repository for Microsoft Products](https://docs.microsoft.com/en-us/windows-server/administration/linux-package-repository-for-microsoft-software)
- [Azure Kinect on Ubuntu 18.04](https://gist.github.com/madelinegannon/c212dbf24fc42c1f36776342754d81bc)

<!-- EOF -->
