cmake_minimum_required(VERSION 2.8.3)
project(squirrel_motion_planner_msgs)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  std_msgs
)

add_service_files(
  FILES
  FoldArm.srv
  UnfoldArm.srv
  SendControlCommand.srv
  PlanEndEffector.srv
  PlanPose.srv
)

generate_messages(
   DEPENDENCIES
   std_msgs
 )

catkin_package(
  CATKIN_DEPENDS message_runtime std_msgs 
)
