import numpy as np
import rospy
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg
from geometry_msgs.msg import PoseStamped
from mpi4py import MPI

class Master():
    def __init__(self, num_workers, max_iteration, comm):
        rospy.init_node('Master', anonymous = True)
        self.num_workers = num_workers
        self.pub_topics = ['worker_%d' %i for i in range(self.num_workers)]
        self.publishers = [rospy.Publisher(name, numpy_msg(Floats), queue_size = 200) for name in self.pub_topics]
        self.sub_topic = ['master_%d' %i for i in range(self.num_workers)]
        self.sum_value = 0
        self.result = []
        self.time = 0
        self.max_iteration = max_iteration
        self.comm = comm
        self.x = np.random.rand(10, 1)
    def run(self):
        # self.subscriber = rospy.Subscriber(self.sub_topic, numpy_msg(Floats), self._call_back, queue_size = 200)

        for iter in range(self.max_iteration):
            self.comm.Barrier()
            recv = []

            for i in range(self.num_workers):
                self.comm.send(self.x, dest = i + 1, tag = iter)

            # Receive results from worker node
            for i in range(self.num_workers):
                data = self.comm.recv(source=MPI.ANY_SOURCE, tag = iter)

                print('Received result from %d' %i, data)


class Worker():
    def __init__(self, worker_index, max_iteration, comm):
        rospy.init_node('Worker%d' %worker_index, anonymous = True)
        self.worker_index = worker_index
        self.sub_topic = '/uav%d/ground_truth_to_tf/pose' %(worker_index+1)
        self.max_iteration = max_iteration
        self.comm = comm
        self.A = np.random.rand(10, 10)
        #self.subscriber = rospy.Subscriber(self.sub_topic, numpy_msg(Floats), self._call_back, queue_size = 200)

    def run(self):
        print('Starting worker %d' %self.worker_index)

        for iter in range(self.max_iteration):
            self.comm.Barrier()

            # Receive data from master node
            recv_x = self.comm.recv(source=0, tag = iter)
            x = rospy.wait_for_message(self.sub_topic, PoseStamped)
            print('UAV %d position is' %self.worker_index, x.pose.position)
            ret = np.matmul(self.A, recv_x)

            self.comm.send(ret, dest=0, tag = iter)
