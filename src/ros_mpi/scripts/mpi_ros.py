#!/usr/bin/env python
from mpi4py import MPI
PKG = 'ros_mpi'
import roslib; roslib.load_manifest(PKG)
import numpy
import rospy
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg
from node import Master
from node import Worker




if __name__== "__main__":
    # MPI initialization.
    comm = MPI.COMM_WORLD
    num_node = comm.Get_size()
    node_id = comm.Get_rank()
    node_name = MPI.Get_processor_name()
    max_iteration = 5

    if node_id == 0:
        master = Master(2, max_iteration, comm)
        master.run()

    if node_id == 1:
        worker = Worker(node_id-1, max_iteration, comm)
        worker.run()

    if node_id == 2:
        worker = Worker(node_id-1, max_iteration, comm)
        worker.run()
