import numpy as np
import rospy
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg

class Master():
    def __init__(self, num_workers):
        rospy.init_node('Master', anonymous = True)
        self.num_workers = num_workers
        self.pub_topics = ['worker_%d' %i for i in range(self.num_workers)]
        self.publishers = [rospy.Publisher(name, numpy_msg(Floats), queue_size = 200) for name in self.pub_topics]
        self.sub_topic = 'master'
        self.sum_value = 0
        self.result = []
        self.time = 0

    def run(self):
        print('master done')
        self.x = np.array([1.0, 2.1, 3.2, 4.3, 5.4, 6.5], dtype=np.float32)
        self.subscriber = rospy.Subscriber(self.sub_topic, numpy_msg(Floats), self._call_back, queue_size = 200)
        for i in range(self.num_workers):
            while self.publishers[i].get_num_connections() < 1:
                nonsense = 1

        for i in range(self.num_workers):
            self.publishers[i].publish(self.x)
        print('master done')

        rospy.spin()
        print('after spin')


    def _call_back(self, data):
        self.time += 1
        self.result.append(data)
        #print(len(self.result))
        if len(self.result) == self.num_workers:
            # do some calculations on the received final result
                # self.sum_value = self.result[0] + self.result[1]
            print('iteration', self.time)
            for i in range(self.num_workers):
                self.publishers[i].publish(self.x)

            self.result = []


class Worker():
    def __init__(self, worker_index):
        rospy.init_node('Worker%d' %worker_index, anonymous = True)
        self.pub_topic = 'master'
        self.publisher = rospy.Publisher(self.pub_topic, numpy_msg(Floats), queue_size = 200)
        self.sub_topic = 'worker_%d' %worker_index
        self.subscriber = rospy.Subscriber(self.sub_topic, numpy_msg(Floats), self._call_back, queue_size = 200)
        while self.publisher.get_num_connections() < 2:
            nonsense = 1

        rospy.spin()

    def _call_back(self, data):
        # do some calculations on the received final result
            # ...
        self.publisher.publish(data)
