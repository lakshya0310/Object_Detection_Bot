cmake_minimum_required(VERSION 3.0.2)
project(yolobot_gazebo)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# Find catkin and any catkin packages
find_package(catkin REQUIRED COMPONENTS
  gazebo_ros
  roscpp
)

# Uncomment and add additional dependencies
# find_package(<dependency> REQUIRED)

catkin_package(
  # INCLUDE_DIRS include
  # LIBRARIES yolobot_gazebo
  CATKIN_DEPENDS gazebo_ros roscpp
  # DEPENDS system_lib
)

# Install directories
install(
  DIRECTORY
    launch
    worlds
  DESTINATION
    ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

# Additional install rules if needed
# install(DIRECTORY include/ DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION})

