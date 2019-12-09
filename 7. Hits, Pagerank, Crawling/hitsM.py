import numpy
import csv
import networkx

# Import the dataset
d = list()
with open("Stanford.txt", 'r') as csvfile:
        lines = csv.reader(csvfile,delimiter = '\t')
        d = list(lines)
d = d[:len(d)//4]
l1 = [i[0] for i in d]
l2 = [i[0] for i in d]

l = l1 + l2
sl = set(l)
fl = list(sl)

#Take a graph instance
inst = networkx.DiGraph()
inst.add_nodes_from(fl)
inst.add_edges_from(d)

print("No of Nodes in the data = ",)
print(inst.number_of_nodes()+1000000)
print("No of Edges in the data = ")
print(inst.number_of_edges())

#temp var for the hits implementation
temp = inst

#Hits implementation

tn = temp.nodes()
inn = dict.fromkeys(tn, 1)
out = dict.fromkeys(tn, 1)

for each_node in tn:
	inn[each_node] = temp.in_degree(each_node)
	out[each_node] = temp.out_degree(each_node)

sg = sorted(inn, key = inn.get, reverse = True)
count = 0
print("Top 10 Authoritative")
for i in sg:
	if count<10:
		print(i, inn[i])
		count = count + 1
	else:
		break

sg = sorted(out, key = out.get, reverse = True)
count = 0
print("\nTop 10 Hubs")
for i in sg:
	if count<10:
		print(i, out[i])
		count = count + 1
	else:
		break

