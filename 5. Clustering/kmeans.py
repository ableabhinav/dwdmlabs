import math
import random
import numpy as np

#datapoint class
class Datapoint:
    def __init__(self,attr,op=''):
        self.attr=attr
        self.op = op

    def display(self):
        print(self.attr,'\t\t',self.op)

#load data
dataset = []
file = open('/media/abh/NEW/BTECH/DWDM/Assignment 5/iris.data','r')
lines = file.readlines()[:-1]
file.close()
#index=0
for line in lines:
    op = line.split(',')[-1]
    attr = list(map(float,line.split(',')[:-1]))
    d1 = Datapoint(attr,op)
    dataset.append(d1)


#mean function
def mean(datapoints):
    mean = [0]*len(datapoints[0].attr)
    count = len(datapoints)
    for i in range(len(datapoints[0].attr)):
        for datapoint in datapoints:
            mean[i] += datapoint.attr[i]
        mean[i] = mean[i]/count
    return mean


#cluster class
class Cluster:
    def __init__(self,datapoints):
        self.datapoints = datapoints
        self.count = len(self.datapoints)
        self.mean = mean(self.datapoints)

    def re_init(self):
        self.datapoints = []
        self.count = 0

    def addDatapoint(self,datapoint):
        self.datapoints.append(datapoint)
        self.count += 1
        self.mean = mean(self.datapoints)

    def display(self):
        print('Mean is ',self.mean)
        print('Datapoints are ')
        for datapoint in self.datapoints:
            datapoint.display()


#function for distance of datapoint from a cluster
def distance(datapoint,cluster):
    p1 = datapoint.attr
    p2 = cluster.mean
    d = 0
    for i in range(len(p2)):
        d += (p1[i]-p2[i])**2
    return math.sqrt(d)

    

#initiate random clusters
clist = []
k=3
for i in range(k):
    rint = random.randint(0,len(dataset)-1)
    c1 = Cluster([dataset[rint]])
    clist.append(c1)

for cluster in clist:
    cluster.display()


#main program
prev_mean = []
for i in range(k):
    prev_mean .append([0]*len(dataset[0].attr))

while True:
    for datapoint in dataset:
        min_dist=1000
        min_cluster=clist[0]
        for cluster in clist:
            if distance(datapoint,cluster) < min_dist:
                min_dist = distance(datapoint,cluster)
                min_cluster = cluster
        min_cluster.addDatapoint(datapoint)

    curr_mean = []
    for cluster in clist:
        curr_mean.append(cluster.mean)

    print('Mean ',curr_mean)

    if curr_mean == prev_mean:
        break

    prev_mean = curr_mean

    for cluster in clist:
        cluster.re_init()

index = 0
for cluster in clist:
    print('Cluster ',index)
    cluster.display()





#125/150