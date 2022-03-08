#!/usr/bin/env python
from mpi4py import MPI
PKG = 'ros_mpi'
import roslib; roslib.load_manifest(PKG)
import numpy
import rospy
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg



def callback(data):
    print rospy.get_name(), "I heard %s"%str(data.data)
    #rospy.signal_shutdown('shutdown_node_id')


if __name__== "__main__":
    # MPI initialization.
    comm = MPI.COMM_WORLD
    num_node = comm.Get_size()
    node_id = comm.Get_rank()
    node_name = MPI.Get_processor_name()

    if node_id == 0:
        pub1 = rospy.Publisher('floats1', numpy_msg(Floats), queue_size=10)
        pub2 = rospy.Publisher('floats2', numpy_msg(Floats), queue_size=10)
        rospy.init_node('talker_%d' %node_id, anonymous=True)
        #r = rospy.Rate(10) # 10hz
        #while not rospy.is_shutdown():
        a = numpy.array([node_id, 1.0, 2.1, 3.2, 4.3, 5.4, 6.5], dtype=numpy.float32)
        while pub1.get_num_connections() < 1:
            b = 1
        pub1.publish(a)
        while pub2.get_num_connections() < 1:
            b = 2
        pub2.publish(a)
        pub1.publish(a)
        pub2.publish(a)
        #rospy.signal_shutdown('shutdown_node_id_%d' %node_id)
        #r.sleep()

    # if node_id == 1:
    #     pub = rospy.Publisher('floats', numpy_msg(Floats))
    #     rospy.init_node('talker_%d' %node_id, anonymous=True)
    #     r = rospy.Rate(10) # 10hz
    #     while not rospy.is_shutdown():
    #         a = numpy.array([node_id, 1.0, 2.1, 3.2, 4.3, 5.4, 6.5], dtype=numpy.float32)
    #         pub.publish(a)
    #         rospy.signal_shutdown('shutdown_node_id_%d' %node_id)
    #         r.sleep()

    if node_id == 1:
        rospy.init_node('listener1')
        rospy.Subscriber("floats1", numpy_msg(Floats), callback)
        rospy.spin()

    if node_id == 2:

        rospy.init_node('listener2')
        rospy.Subscriber("floats2", numpy_msg(Floats), callback)
        rospy.spin()
