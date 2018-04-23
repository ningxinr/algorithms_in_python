import re

f = open('clustering.txt', 'r')
rangeV = int(f.readline())
e = dict()

for line in f:
	listV = []
	items = line.split()
	listV.append(int(items[0]))
	listV.append(int(items[1]))
	if int(items[2]) in e:
		e[int(items[2])].append(listV)
	else:
		e.update({int(items[2]): [listV]})

unionFind = dict()

sortedKeys = e.keys()
sortedKeys.sort()
cluster = dict()
rcluster = dict()

for i in range(rangeV):
	cluster.update({i+1:[i+1]})
	rcluster.update({i+1:i+1})

flag = 0

for key in sortedKeys:
	for edge in e[key]:
		if len(cluster.keys()) == 4 and rcluster[edge[0]] != rcluster[edge[1]]:
			flag = 1
			break
		elif len(cluster.keys()) > 4 and rcluster[edge[0]] != rcluster[edge[1]]:
			if len(cluster[rcluster[edge[0]]]) > len(cluster[rcluster[edge[1]]]):
				for cedge in cluster.pop(rcluster[edge[1]]):
					rcluster[cedge] = rcluster[edge[0]]
					cluster[rcluster[edge[0]]].append(cedge)
			else:
				for cedge in cluster.pop(rcluster[edge[0]]):
					rcluster[cedge] = rcluster[edge[1]]
					cluster[rcluster[edge[1]]].append(cedge)
	if flag == 1:
		break

print 'cluster number: ',  len(cluster.keys())
print 'spacing', key
 
