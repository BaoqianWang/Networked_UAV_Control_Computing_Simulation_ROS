#! /usr/bin/env python
import rospy
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
import json
PKG = 'pos_controller'
from time import sleep

import roslib; roslib.load_manifest(PKG)

filename = '/home/smile/nac_sim/src/pos_controller/scripts/path.txt'
with open(filename, 'r') as fd:
    path = json.load(fd)
    print(path['uav1'])
