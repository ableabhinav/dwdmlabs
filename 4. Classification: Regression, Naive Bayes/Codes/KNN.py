
import numpy as np
import heapq
import math

def load_data():
    x = []
    y_train = []
    f = open('train.data', 'r')
    dict = {'Iris-versicolor': 1, 'Iris-setosa': 2, 'Iris-virginica': 3}
    for s in f.readlines():
        s_list = s.split(',')[0:len(s)]
        x.append(list(map(float, s_list[:len(s_list) - 1])))  # split input and output and create arrays
        y_train.append(float(dict[s_list[len(s_list) - 1].strip()]))
    x_train = np.array(x, dtype=float)
    y_train = np.array(y_train, dtype=float)

    x = []
    y_test = []
    f = open('test.data', 'r')
    for s in f.readlines():
        s_list = s.split(',')[0:len(s)]
        x.append(list(map(float, s_list[:len(s_list) - 1])))  # split input and output and create arrays
        y_test.append(float(dict[s_list[len(s_list) - 1].strip()]))
    x_test = np.array(x, dtype=float)
    y_test = np.array(y_test, dtype=float)
    return x_train, y_train, x_test, y_test

c = 3 # number of classes
n = 5 # number of parameters


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
        self._count = 0
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
        self._count += 1

    def pop(self):
        self._count -= 1
        return heapq.heappop(self._queue)[-1]

    def queue_size(self):
        return self._count

    def is_empty(self):
        return self._count == 0


def euclidean_distance(point_A, point_B):
    return math.sqrt(np.sum((point_A.attribute_values - point_B.attribute_values) ** 2))


class DataPoint:
    def __init__(self, values, my_class=-1):
        self.attribute_values = values
        self.my_class = my_class


def KNN_classify(x_train, y_train, x_test, n_neighbours=5):
    count = y_test.size
    train_count = y_train.size
    result = np.array([0]*count)
    for i in range( count ):
        q = PriorityQueue()
        test_point = DataPoint(x_test[i])
        for j in range(train_count):
            train_point = DataPoint(x_train[j], y_train[j])
            dist1 = euclidean_distance(train_point, test_point)

            if q.queue_size() < n_neighbours :
                q.push(train_point, dist1)
            else:
                queue_top = q.pop()
                dist2 = euclidean_distance(queue_top, test_point)
                if dist1 < dist2:
                    q.push(train_point, dist1)
                else:
                    q.push(queue_top, dist2)

        class_count = [0] *(c + 1)
        while not q.is_empty():
            top = q.pop()
            class_count[int(top.my_class)] += 1

        # print class_count

        for j in range(1, c + 1):
            if class_count[j] == max(class_count):
                result[i] = j
                break
    return result


x_train, y_train, x_test, y_test = load_data()

predicted = KNN_classify(x_train, y_train, x_test, 5)

for j in range(predicted.size):
    print ('Expected :', y_test[j], '  Predicted:', predicted[j])
