# Message generated for the scan safety observer.
std_msgs/Header header 
bool[] safe_readings               # Which readings are safe
bool is_safe                       # Is the scan safe
float32[] range_velocities         # Current variation of the range value along the beam direction
float32 max_safety_range_velocity  # Maximum variation allowed along beam directions
float32 unsafe_range               # Range within which rapid movements are considered unsafe
