cmake_minimum_required(VERSION 3.0.2)
project(yolobot_control)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# Add warning flags for GCC/Clang
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find catkin and any catkin packages
find_package(catkin REQUIRED COMPONENTS
  rospy
  geometry_msgs
  sensor_msgs
  std_msgs
)

# Declare a catkin package
catkin_package()

# Install Python scripts and launch files
catkin_install_python(PROGRAMS
  scripts/robot_control.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

# Install launch files
install(
  DIRECTORY
    launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

# Additional dependencies for teleop_twist_keyboard (this is not necessary for CMake)
# but could be added if you need to declare any extra Python packages here.

