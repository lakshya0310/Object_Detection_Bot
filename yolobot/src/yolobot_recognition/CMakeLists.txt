cmake_minimum_required(VERSION 3.0.2)
project(yolobot_recognition)

## Compile as C++14, supported in ROS Melodic and newer
add_compile_options(-std=c++14)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  rospy
  sensor_msgs
  cv_bridge
  image_transport
)

## System dependencies are found with CMake's conventions
find_package(OpenCV REQUIRED)

## Declare catkin package
catkin_package(
  CATKIN_DEPENDS rospy sensor_msgs cv_bridge image_transport
)

## Specify additional locations of header files
include_directories(
  ${catkin_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
)

## Install Python scripts
catkin_install_python(PROGRAMS
  scripts/ros_recognition_yolo.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

