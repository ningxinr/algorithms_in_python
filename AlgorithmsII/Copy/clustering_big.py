f = open('clustering_big.txt', 'r')
param = f.readline().split()
rangeV = int(param[0])
lenV = int(param[1])
e = dict()
listV = []

for line in f:
	cnt = 0
	v = []
	items = line.split()
	for item in items:
		if item == '1':
			cnt += 1
		v.append(int(item))
	if cnt in e:
		e[cnt].append(len(listV))
	else:
		e.update({cnt: [len(listV)]})
	listV.append(v)
sortedKeys = e.keys()
sortedKeys.sort()
cluster = dict()
rcluster = dict()

for i in range(rangeV):
	cluster.update({i:[i]})
	rcluster.update({i:i})

for i in range(2):
	for key in sortedKeys:
		for nV1 in e[key]:
			for nV2 in e[key + i]:
				if nV1 == nV2 or rcluster[nV1] == rcluster[nV2]:
					continue
				else:
					cnt = 0
					for idx in range(lenV):
						if listV[nV1][idx] != listV[nV2][idx]:
							cnt += 1
						if cnt > 2:
							break
					if cnt < 3:
						if len(cluster[rcluster[nV1]]) > len(cluster[rcluster[nV2]]):
							for cedge in cluster.pop(rcluster[nV2]):
								rcluster[cedge] = rcluster[nV1]
								cluster[rcluster[nV1]].append(cedge)
						else:
							for cedge in cluster.pop(rcluster[nV1]):
								rcluster[cedge] = rcluster[nV2]
								cluster[rcluster[nV2]].append(cedge)
#				print 'nV1: ', nV1, 'nV2: ', nV2, 'cluster number: ',  len(cluster.keys())

print 'cluster number: ',  len(cluster.keys())
 
