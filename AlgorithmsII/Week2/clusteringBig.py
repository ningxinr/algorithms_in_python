import math

f = open('clustering_big.txt', 'r')
param = f.readline().split()
rangeV = int(param[0])
lenV = int(param[1])
listV = dict()
listRV = dict()
length = 0

for line in f:
	items = line.split()
	ints = []
	for item in items:
		ints.append(int(item))
	key = tuple(ints)
	if key in listV:
		listV[key].append(length)
	else:
		listV.update({key: [length]})
	listRV.update({length: key})
	length += 1

cluster = dict()
rcluster = dict()

for i in range(rangeV):
	cluster.update({i:[i]})
	rcluster.update({i:i})

def merge(i, j) :
	if len(cluster[rcluster[i]]) > len(cluster[rcluster[j]]):
		for cedge in cluster.pop(rcluster[j]):
			rcluster[cedge] = rcluster[i]
			cluster[rcluster[i]].append(cedge)
	else:
		for cedge in cluster.pop(rcluster[i]):
			rcluster[cedge] = rcluster[j]
			cluster[rcluster[j]].append(cedge)

for i in range(rangeV):
	for j in listV[listRV[i]]:
		if i == j or rcluster[i] == rcluster[j]:
			continue
		merge(i, j)
		print 'i: ', i, 'j: ', j, 'cluster number: ',  len(cluster.keys())

for i in range(rangeV):
	for m in range(lenV):
		mutV = list(listRV[i])
		mutV[m] = int(mutV[m] != 1)
		if tuple(mutV) in listV:
			for j in listV[tuple(mutV)]:
				if rcluster[i] == rcluster[j]:
					continue
				merge(i, j)
				print 'i: ', i, 'j: ', j, 'cluster number: ',  len(cluster.keys())

for i in range(rangeV):
	for m in range(lenV):
		for n in range(m, lenV):
			mutV = list(listRV[i])
			mutV[m] = int(mutV[m] != 1)
			mutV[n] = int(mutV[n] != 1)
			if tuple(mutV) in listV:
				for j in listV[tuple(mutV)]:
					if rcluster[i] == rcluster[j]:
						continue
					merge(i, j)
					print 'i: ', i, 'j: ', j, 'cluster number: ',  len(cluster.keys())

print 'cluster number: ',  len(cluster.keys())
 
