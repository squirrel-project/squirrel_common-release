# Scene Object
#
# An object with all its attributes as stored in the scene database.
#
# author: Michael Zillich, michael.zillich@tuwien.ac.at

# when the object was last seen
std_msgs/Header header

# a unique meaningless ID, e.g. 'object376', not to be confused with any
# meaningful label, object name etc.
string id

# the object's category, which can be:
# - narrow ('lego-police-truck'), i.e. typically an instance label as
#   returned by a recogniser
# - broad ('truck'), i.e. typically a class label as returned by a classifier
# - unknown, i.e. just 'stuff' where we don't know what is is
string category

# the object's pose, typically given in the map frame
geometry_msgs/Pose pose

# the object's point cloud as segmented from the scene
sensor_msgs/PointCloud2 cloud

# A bounding cylinder, aligned with upwards pointing z-axis and resting on the
# floor. It's center is (pose.x, pose.y, 0)
squirrel_object_perception_msgs/BCylinder bounding_cylinder
