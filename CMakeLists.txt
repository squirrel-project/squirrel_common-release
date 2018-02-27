cmake_minimum_required(VERSION 2.8.3)
project(squirrel_planning_msgs)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  diagnostic_msgs
)

add_service_files(
  FILES
  CallAction.srv
)

generate_messages(
  DEPENDENCIES
  diagnostic_msgs
)

catkin_package(
 CATKIN_DEPENDS
    message_runtime
    diagnostic_msgs
)
