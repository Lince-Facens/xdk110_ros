# xdk110_ros

The firmware for the XDK110 Bosch sensor can be found at https://github.com/Lince-Facens/Xdk110RosSerial
After flashing the firmware, clone this repository into your catkin workspace and compile it.
Launch the node: `rosrun xdk110_ros node.py`

At this moment this driver only supports the Imu sensor data, in the future the other sensors from XDK110 will be supported.
