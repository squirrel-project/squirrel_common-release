cmake_minimum_required(VERSION 2.8.3)
project(squirrel_object_perception_msgs)

find_package(catkin REQUIRED COMPONENTS
  actionlib
  actionlib_msgs
  geometry_msgs
  message_generation
  octomap_msgs
  sensor_msgs
  std_msgs
)

add_message_files(
  FILES
  BBox.msg
  Classification.msg
  Saliency.msg
  ViewpointEntropy.msg
)

add_service_files(
  FILES
  Classify.srv
  ClearFixation.srv
  CoveragePlan.srv
  CoveragePlanFile.srv
  EntropyMap.srv
  EntropyMapViz.srv
  FixatePosition.srv
  GetSaliency3DSymmetry.srv
  GetSaliencyColor.srv
  GetSaliencyHeight.srv
  GetSaliencyItti.srv
  GetSaliencyLocation.srv
  GetSaliencySurfaceOrientation.srv
  GetSaliencySymmetry.srv
  LookAtImagePosition.srv
  LookAtPosition.srv
  Recognize.srv
  Segment.srv
  SegmentInit.srv
  SegmentOnce.srv
  SegmentVisualizationInit.srv
  SegmentVisualizationOnce.srv
  SegmentsToObjects.srv
  StartObjectTracking.srv
  StopObjectTracking.srv
)

add_action_files(
  FILES
  LookForObjects.action
)

generate_messages(
  DEPENDENCIES
  actionlib_msgs
  actionlib_msgs
  geometry_msgs
  octomap_msgs
  sensor_msgs
  std_msgs
)

catkin_package(
#  INCLUDE_DIRS include
 #  LIBRARIES squirrel_object_perception_msgs
 CATKIN_DEPENDS
    #  DEPENDS system_lib

    actionlib_msgs
    geometry_msgs
    message_runtime
    octomap_msgs
    sensor_msgs
    std_msgs
)

install(DIRECTORY include/${PROJECT_NAME}/ DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION})