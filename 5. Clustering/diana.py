import math

#class for datapoint
class Datapoint:
    count = 0
    def __init__(self,attr,op):
        self.attr = attr
        self.op = op
        Datapoint.count += 1

    def display(self):
        print(self.attr,' => ',self.op)

#class for cluster
class Cluster:
    def __init__(self,datapoints):
        self.datapoints = datapoints
        self.count = len(self.datapoints)

    def addDatapoint(self,datapoint):
        self.datapoints.append(datapoint)
        self.count += 1

    def display(self,str=''):
        print('Cluster ',str,' has count ',self.count)
        for datapoint in self.datapoints:
            datapoint.display()

#load data from file
file = open('iris.data','r')
lines = file.readlines()[:-1]
file.close()

dataset = []
for line in lines:
    op = line.split(',')[-1]
    attr = list(map(float,line.split(',')[:-1]))
    d1 = Datapoint(attr,op)
    dataset.append(d1)

'''
#display dataset
for datapoint in dataset:
    datapoint.display()
'''

#function for distance between datapoints
def distance(d1,d2):
    d1 = d1.attr
    d2 = d2.attr

    dist = 0
    for i in range(len(d1)):
        dist += (d1[i]-d2[i])**2

    return math.sqrt(dist)

#function for finding max separated points in a cluster
def maxSeparated(cluster):
    datapoints = cluster.datapoints
    max_dist = 0
    m1=0
    mj=1
    for i in range(len(datapoints)):
        for j in range(i+1,len(datapoints)):
            if distance(datapoints[i],datapoints[j])>max_dist:
                max_dist = distance(datapoints[i],datapoints[j])
                mi = i
                mj = j
    return datapoints[mi],datapoints[mj]

#function to form two child clusters from two seeds in a single parent cluster
def formClusters(cluster,d1,d2):
    datapoints = cluster.datapoints
    c1 = []
    c2 = []
    for d in datapoints:
        if distance(d,d1)<distance(d,d2):
            c1.append(d)
        else:
            c2.append(d)

    c1 = Cluster(c1)
    c2 = Cluster(c2)
    return c1,c2


#main program
clist = [Cluster(dataset)]

k = 3
while len(clist)!=k:
    curr_cluster = clist[0]
    d1,d2 = maxSeparated(curr_cluster)
    c1,c2 = formClusters(curr_cluster,d1,d2)
    clist.append(c1)
    clist.append(c2)
    del clist[0]

for i in range(len(clist)):
    clist[i].display(i)


# 118/150 => 78.66 %
