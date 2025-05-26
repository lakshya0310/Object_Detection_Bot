cmake_minimum_required(VERSION 3.0.2)
project(yolobot_description)

# Set default C++ standard
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# Add warning flags for GCC/Clang
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find catkin and required packages
find_package(catkin REQUIRED COMPONENTS
  urdf
  xacro
)

# Declare the catkin package
catkin_package()

# Install URDF and launch files
install(
  DIRECTORY
    launch
    robot
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

