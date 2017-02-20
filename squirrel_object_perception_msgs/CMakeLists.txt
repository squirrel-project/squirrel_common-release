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
  BCylinder.msg
  Classification.msg
  DynamicObject.msg
  LumpToDB.msg
  ObjectToDB.msg
  Saliency.msg
  StampedDynamicObject.msg
  ViewpointEntropy.msg
  SceneObject.msg
)

add_service_files(
  FILES
  ActiveExplorationNBV.srv
  Classify.srv
  CoveragePlan.srv
  CoveragePlanFile.srv
  EntropyMap.srv
  EntropyMapViz.srv
  FindDynamicObjects.srv
  GetSaliency3DSymmetry.srv
  GetSaliencyColor.srv
  GetSaliencyHeight.srv
  GetSaliencyItti.srv
  GetSaliencyLocation.srv
  GetSaliencySurfaceOrientation.srv
  GetSaliencySymmetry.srv
  Recognize.srv
  Recognize2d.srv
  Segment.srv
  SegmentInit.srv
  SegmentOnce.srv
  SegmentVisualizationInit.srv
  SegmentVisualizationOnce.srv
  SegmentsToObjects.srv
  StartObjectTracking.srv
  StopObjectTracking.srv
  StartInstanceTracking.srv
  StopInstanceTracking.srv
  StartLumpTracking.srv
  StopLumpTracking.srv
)

add_action_files(
  FILES
  LookForObjects.action
  GraspObject.action
)

generate_messages(
  DEPENDENCIES
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
