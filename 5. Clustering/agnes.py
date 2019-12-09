import math
import numpy as np

class Datapoint:
    dp_count = 0
    def __init__(self,attr,cat):
        self.attr = attr
        self.cat = cat
        Datapoint.dp_count += 1

    def displayDatapoint(self,opt=''):
        print('Datapoint ',opt,' is ',self.attr,' of category ',self.cat)

    def displayCount(self):
        print('Datapoint count is ',Datapoint.dp_count)


#get data from iris.data

file = open('iris.data','r')
lines = file.readlines()[:-1]
dataset = {}
file.close()

count=0
for line in lines:
    cat = line.split(',')[-1]
    attr = list(map(float,line.split(',')[:4]))
    d1 = Datapoint(attr,cat)
    count+=1
    dataset[count]=d1

"""
#normalize the data
alist = {}
for i in range(len(dataset[1].attr)):
    alist[i]=[]
    for index in dataset:
        alist[i].append(dataset[index].attr[i])

mean={}
std={}
for i in range(len(dataset[1].attr)):
    mean[i] = np.mean(alist[i])
    std[i] = np.std(alist[i])
        
for index in dataset:
    dp = dataset[index]
    for i in range(len(dp.attr)):
        dp.attr[i] = (dp.attr[i]-mean[i])/std[i]
"""

#function for finding distance between 2 datapoints
def dist(d1,d2):
    s=0
    for i in range (len(d1)):
        s += (d1[i]-d2[i])**2
    return math.sqrt(s)


#cluster class
class Cluster:
    index=0
    def __init__(self,datapoints,cluster1=None,cluster2=None):

        if cluster1==None and cluster2==None:
            self.datapoints = datapoints
            self.dps_count = len(datapoints)

        else:    
            self.datapoints=(cluster1.datapoints)+(cluster2.datapoints)
            self.dps_count = len(self.datapoints)

        Cluster.index += 1
        self.name = Cluster.index

    def displayCluster(self):
        print(self.name,' => ')
        for datapoint in self.datapoints:
            datapoint.displayDatapoint()

    def addDatapoints(self,datapoints):
        self.datapoints.add(datapoints)
        self.dps_count += len(datapoints)

    def distance(cluster1,cluster2):
        d=0
        count=0
        for point1 in cluster1.datapoints:
            for point2 in cluster2.datapoints:
                d += dist(point1.attr,point2.attr)
                #d = min(d,dist(point1.attr,point2.attr))
                count +=1
        return d/count        

#initial clusters
clist=[]
for i in dataset:
    c1 = Cluster([dataset[i]])
    clist.append(c1);



#main function
while len(clist)!=3:

    cdist=1000
    mi=0
    mj=0
    for i in range(len(clist)):
        for j in range(i+1,len(clist)):
            curr = Cluster.distance(clist[i],clist[j])
            if curr < cdist:
                cdist = curr
                mi = i
                mj = j

    cnew = Cluster(None,clist[mi],clist[mj])
    del clist[mi]
    del clist[mj-1]
    clist.append(cnew)
    print(len(clist))

for cluster in clist:
    cluster.displayCluster()


#136/150