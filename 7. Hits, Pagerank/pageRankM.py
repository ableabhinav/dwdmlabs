import numpy as np
import csv
import networkx

d = list()
with open("Stanford.txt", 'r') as csvfile:
        lines = csv.reader(csvfile,delimiter = '\t')
        d = list(lines)
d = d[0:10000]
for i in range(len(d)):
        for j in range(2):
                d[i][j] = int(d[i][j])
l1 = [i[0] for i in d]
l2 = [i[1] for i in d]

l = l1 + l2
sl = set(l)
fl = list(sl)
print(len(fl))
#Take a graph instance
inst = networkx.DiGraph()
inst.add_nodes_from(fl)
inst.add_edges_from(d)

npmat = networkx.to_numpy_matrix(inst)

row,col = npmat.shape

ranks = np.ones((row,1))
print("rows = ",col)
ranks = ranks/row

npmatT = npmat.T
npmatT = np.matrix(npmatT,dtype = float)

for i in range(col):
        cnt = 0
        for k in range(row):
                if npmatT[i,k] == 1:
                        cnt+=1
        for j in range(row):
                if cnt == 0:
                        cnt = 1
                npmatT[i,j] = npmatT[i,j] / cnt
fmat = npmatT.T
print(fmat.shape)
ranks = np.dot(fmat, ranks)
print("Ranks of the page are: ")
#print ranks

lr = list(ranks)
sll = sorted(lr,reverse = True)
for j in range(10):
	temp = sll[j]
	val = lr.index(temp)
	#print("val= ", val)
	print(j+1, fl[val],temp)
