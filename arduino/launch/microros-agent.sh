#!/bin/bash
/home/pi/microros_ws/install/micro_ros_agent/lib/micro_ros_agent/micro_ros_agent serial --dev /dev/serial/by-id/usb-Silicon_Labs_CP2102N_USB_to_UART_Bridge_Controller_0010-if00-port0 -b 115200 --ros-args -r __node:=microros_arduino_serial_node
