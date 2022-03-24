#!/usr/bin/env python

PKG = 'ros_mpi'

import roslib; roslib.load_manifest(PKG)

import rospy
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg
import argparse
#

# def parse_args():
#     parser = argparse.ArgumentParser("ROS python argument test")
#     # Environment
#     parser.add_argument("--index", type=int, default=1, help="UAV index")
#     # Core training parameters
#     return parser.parse_args()

if __name__ == '__main__':
    ns = rospy.get_namespace()
    index = rospy.get_param(ns + "/index")
    print('hello world', index)
