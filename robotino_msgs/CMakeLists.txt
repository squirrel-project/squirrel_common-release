cmake_minimum_required(VERSION 2.8.3)
project(robotino_msgs)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  std_msgs
  message_generation
)

## Generate messages in the 'msg' folder
 add_message_files(
   FILES
   AnalogReadings.msg
   EncoderReadings.msg
   MotorReadings.msg
   SetBHAPressures.msg
   BHAReadings.msg
   GrapplerReadings.msg
   NorthStarReadings.msg
   SetGrapplerAxes.msg
   DigitalReadings.msg
   GripperState.msg
   PowerReadings.msg
   SetGrapplerAxis.msg
 )

# Generate services in the 'srv' folder
 add_service_files(
   FILES
   ResetOdometry.srv
   SetEncoderPosition.srv
   SetGripperState.srv 
   ClearFixation.srv
   FixatePanTilt.srv
   FixatePosition.srv
   LookAtImagePosition.srv
   LookAtPanTilt.srv
   LookAtPosition.srv
)
## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   geometry_msgs
   std_msgs
 )

catkin_package(
  CATKIN_DEPENDS 
     message_runtime 
     std_msgs 
     geometry_msgs
)
