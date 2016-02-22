cmake_minimum_required(VERSION 2.8.3)
project(squirrel_waypoint_msgs)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  message_generation
  std_msgs
)

#add_message_files(
#  FILES
#)

add_service_files(
  FILES

  ExamineWaypoint.srv
)

#add_action_files(
#  FILES
#)

generate_messages(
  DEPENDENCIES
  geometry_msgs
  std_msgs
)

catkin_package(
#  INCLUDE_DIRS include
 #  LIBRARIES squirrel_object_perception_msgs
 CATKIN_DEPENDS
    #  DEPENDS system_lib

    geometry_msgs
    message_runtime
    std_msgs
)
