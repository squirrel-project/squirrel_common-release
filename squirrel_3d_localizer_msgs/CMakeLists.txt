cmake_minimum_required(VERSION 2.8.3)
project(squirrel_3d_localizer_msgs)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  message_generation
  std_msgs
)

add_service_files(
  FILES
  ToggleSensors.srv
  SetMap.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
  geometry_msgs
)


catkin_package(
  CATKIN_DEPENDS geometry_msgs message_runtime std_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
