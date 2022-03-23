'''
Author: BaoqianWang
Date Created: 03/16/2022
Description: Waypoint follower
'''
import rospy, tf
import geometry_msgs.msg, nav_msgs.msg
from math import *
import numpy as np
from time import sleep
import time
import json
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import PoseStamped


class WaypoingFollower:
    '''
    waypoing following implementation
    '''
    def __init__(self, pos0, node_name="waypointfollower"):
        rospy.init_node(node_name)
        self.pose = [pos0[0], pos0[1], pos0[2]]
        # self.ini_pos = initial_pos
        self.kdx = 0.5
        self.kdy = 0.5
        self.kdz = 0.5
        self.sub_topic = '/ground_truth_to_tf/pose'
        self.pub_topic = '/cmd_vel'
        self.distThresh = 0.3

    def get_pos(self, message):
        # Implementation of proportional position control
        self.pose = [message.pose.position.x, message.pose.position.y, message.pose.position.z]



    def run(self):
        msg = geometry_msgs.msg.Twist()
        pub = rospy.Publisher(self.pub_topic, geometry_msgs.msg.Twist, queue_size=10)
        rospy.Subscriber(self.sub_topic, PoseStamped, self.get_pos)

        filename='path.txt'
        with open(filename, 'r') as fd:
            path=json.load(fd)


        # Proportional Controller
        for goal_x, goal_y, goal_z in zip(path['x'], path['y'], path['z']):
            print('Goal is', goal_x, goal_y, goal_z)
            print('Current position: x=%4.1f, y=%4.1f, z=%4.1f'%(self.pose[0], self.pose[1], self.pose[2]))
            distance = sqrt((self.pose[0]-goal_x)**2 + (self.pose[1]-goal_y)**2 + (self.pose[2]-goal_z)**2)
            while distance > self.distThresh:
                distance = sqrt((self.pose[0]-goal_x)**2 + (self.pose[1]-goal_y)**2 + (self.pose[2]-goal_z)**2)

                vx, vy, vz = self.kdx * (goal_x- self.pose[0]), self.kdy * (goal_y- self.pose[1]), self.kdz * (goal_z- self.pose[2])

                # Publish
                msg.linear.x = vx
                msg.linear.y = vy
                msg.linear.z = vz
                pub.publish(msg) # control frequency
                print('control_callback: x = %4.1f, y = %4.1f, z = %4.1f, dist = %4.2f, vx = %4.2f, vy = %4.2f, vz = %4.2f' %(self.pose[0], self.pose[1], self.pose[2], distance, vx, vy, vz))

        # print('Third', v,u)
        # cmdmsg.data = [0, u]
        # cmdpub.publish(cmdmsg)


if __name__ == "__main__":
    sleep(3)
    waypoint_follower = WaypoingFollower([0, 0, 0.3])
    waypoint_follower.run()
    rospy.spin()
