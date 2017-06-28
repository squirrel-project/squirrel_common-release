cmake_minimum_required(VERSION 2.8.3)
project(squirrel_footprint_observer_msgs)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  message_generation
  message_runtime
)

add_service_files(
  FILES
  get_footprint.srv
)

generate_messages(
  DEPENDENCIES
  geometry_msgs
)


catkin_package(
 CATKIN_DEPENDS geometry_msgs message_generation message_runtime
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
