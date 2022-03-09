import numpy as np
import rospy
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg

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

    def run(self):
        self.x = np.array([1.0, 2.1, 3.2, 4.3, 5.4, 6.5], dtype=np.float32)
        # self.subscriber = rospy.Subscriber(self.sub_topic, numpy_msg(Floats), self._call_back, queue_size = 200)


        for iter in range(self.max_iteration):
            self.comm.Barrier()
            recv = []
            print(iter, 'start')
            # for i in range(self.num_workers):
            #     while self.publishers[i].get_num_connections() < 1:
            #         nonsense = 1
            print(iter, 'connected')
            # Send x to each worker node
            # for i in range(self.num_workers):
            #     self.publishers[i].publish(self.x)

            print(iter, 'published')
            # for i in range(self.num_workers):
            #     value = rospy.wait_for_message(self.sub_topic[i], numpy_msg(Floats))
            #     recv.append(value)
            print(recv)
            print(iter, 'end')

class Worker():
    def __init__(self, worker_index, max_iteration, comm):
        rospy.init_node('Worker%d' %worker_index, anonymous = True)
        self.worker_index = worker_index
        self.pub_topic = 'master_%d' %worker_index
        self.publisher = rospy.Publisher(self.pub_topic, numpy_msg(Floats), queue_size = 200)
        self.sub_topic = 'worker_%d' %worker_index
        self.max_iteration = max_iteration
        self.comm = comm
        #self.subscriber = rospy.Subscriber(self.sub_topic, numpy_msg(Floats), self._call_back, queue_size = 200)

    def run(self):
        print('Starting worker %d' %self.worker_index)


        for iter in range(self.max_iteration):
            self.comm.Barrier()
            # Receive data from master node
            #x = rospy.wait_for_message(self.sub_topic, numpy_msg(Floats))
            # Do some computation with the received data
            y = np.array([1.0, 2.1, 3.2, 4.3, 5.4, 6.5], dtype=np.float32)
            y[0] = 10 * (self.worker_index + 1)

            # while self.publisher.get_num_connections() < 1:
            #     nonsense = 1
            # Send data to master node
            #self.publisher.publish(y)
            print('worker done')
