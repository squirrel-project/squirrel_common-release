cmake_minimum_required(VERSION 2.8.3)
project(squirrel_hri_msgs)

find_package(catkin REQUIRED COMPONENTS
  actionlib
  actionlib_msgs
  geometry_msgs
  rospy
  std_msgs
  message_generation
)

 add_message_files(DIRECTORY msg
   FILES
   Expression.msg
 )

## Generate messages in the 'action' folder
 add_action_files(DIRECTORY action
   FILES
   FollowChild.action
 )

generate_messages(
  DEPENDENCIES
  actionlib_msgs
  actionlib_msgs
  geometry_msgs
  std_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES squirrel_speech_rec
  CATKIN_DEPENDS rospy std_msgs message_runtime actionlib_msgs geometry_msgs
#  DEPENDS system_lib
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
