cmake_minimum_required(VERSION 2.8.3)
project(squirrel_view_controller_msgs)

find_package(catkin REQUIRED COMPONENTS
  actionlib
  actionlib_msgs
  geometry_msgs
  std_msgs
  message_generation
)

# Generate services in the 'srv' folder
 add_service_files(
   FILES
   ClearFixation.srv
   FixatePanTilt.srv
   FixatePosition.srv
   LookAtImagePosition.srv
   LookAtPanTilt.srv
   LookAtPosition.srv
)


# Generate actions in the 'action' folder
  add_action_files(
    FILES
    FixateOnPose.action
)
## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs
  actionlib_msgs
  geometry_msgs
)

catkin_package(
  CATKIN_DEPENDS
    actionlib_msgs
    message_runtime 
    std_msgs 
)
