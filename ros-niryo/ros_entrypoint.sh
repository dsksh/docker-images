#!/bin/bash
set -e

# setup ros environment
source "/catkin_ws_niryo_ned/devel/setup.bash"
exec "$@"
