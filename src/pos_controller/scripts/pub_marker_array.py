#! /usr/bin/env python
import rospy
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
import json
PKG = 'pos_controller'
from time import sleep

import roslib; roslib.load_manifest(PKG)
sleep(5)
rospy.init_node('rviz_marker_array')

marker_pub = rospy.Publisher("/visualization_marker_array", MarkerArray, queue_size = 2)

filename = '/home/smile/nac_sim/src/pos_controller/scripts/path.txt'
with open(filename, 'r') as fd:
    path = json.load(fd)

markerArray = MarkerArray()
i = 0

for x, y, z in zip(path['x'], path['y'], path['z']):
    marker = Marker()
    marker.header.frame_id = "/world"
    marker.header.stamp = rospy.Time.now()

    # set shape, Arrow: 0; Cube: 1 ; Sphere: 2 ; Cylinder: 3
    marker.type = 1
    marker.id = i

    # Set the scale of the marker
    marker.scale.x = 0.2
    marker.scale.y = 0.2
    marker.scale.z = 0.2

    # Set the color
    marker.color.r = 0.0
    marker.color.g = 1.0
    marker.color.b = 0.0
    marker.color.a = 1.0

    # Set the pose of the marker
    marker.pose.position.x = x
    marker.pose.position.y = y
    marker.pose.position.z = z
    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 1.0

    markerArray.markers.append(marker)
    i += 1


while not rospy.is_shutdown():
  marker_pub.publish(markerArray)
  rospy.rostime.wallsleep(1.0)
