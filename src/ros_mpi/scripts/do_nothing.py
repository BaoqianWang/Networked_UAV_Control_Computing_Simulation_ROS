#!/usr/bin/env python

PKG = 'ros_mpi'

import roslib; roslib.load_manifest(PKG)

import rospy
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg

#

if __name__ == '__main__':
    print('hello world')
