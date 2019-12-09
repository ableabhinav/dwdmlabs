import math

#class for datapoint
class Datapoint:
    count = 0
    def __init__(self,attr,op):
        self.attr = attr
        self.op = op
        self.cluster = -1 #unclassified
        Datapoint.count += 1
        
    def display(self):
        print(self.attr,' => ',self.cluster,' || ',self.op)

#load dataset
file = open('iris.data','r')
lines = file.readlines()[:-1]
file.close()

dataset = []
for line in lines:
    op = line.split(',')[-1]
    attr = list(map(float,line.split(',')[:-1]))
    d1 = Datapoint(attr,op)
    dataset.append(d1)

#functions
def distance(d1,d2):
    d1 = d1.attr
    d2 = d2.attr
    dist = 0
    for i in range(len(d1)):
        dist += (d1[i]-d2[i])**2
    return math.sqrt(dist)

def epsilonNeighbours(datapoint):
    eps_list = []
    for d in dataset:
        if distance(d,datapoint)<=eps :
            eps_list.append(d)
    return eps_list

def expandCluster(eps_list,cluster):
    new_list = []
    for nbr in eps_list:
        if nbr.cluster == -1 or nbr.cluster == -2:
            nbr.cluster = cluster
            new_list.append(nbr)
        else:
            if nbr.cluster != cluster:
                nbr.cluster = -3
    return new_list

def process(tmpset):
    for datapoint in tmpset:
        eps_nbrs = epsilonNeighbours(datapoint)
        if len(eps_nbrs) < min_nbrs:
            if datapoint == tmpset[0]:
                datapoint.cluster = -2 #noise or boundary point
        else:
            eps_nbrs = expandCluster(eps_nbrs,datapoint.cluster)
            tmpset = tmpset + eps_nbrs


#main program
eps = 3
min_nbrs = 40

cluster_id = 0
tmpset = []    
for datapoint in dataset:
    if datapoint.cluster == -1: #if unclassified
        cluster_id += 1
        datapoint.cluster = cluster_id
        tmpset = []
        tmpset.append(datapoint)
        process(tmpset)

#display
final_clusters = {}

for datapoint in dataset:    
    if datapoint.cluster not in final_clusters:
        final_clusters[datapoint.cluster] = []
    final_clusters[datapoint.cluster].append(datapoint)

for index in final_clusters:
    dlist = final_clusters[index]
    print(index,' => count is ',len(dlist))
    for datapoint in dlist:
        datapoint.display()
