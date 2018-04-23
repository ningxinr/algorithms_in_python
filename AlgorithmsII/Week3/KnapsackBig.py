import sys
import random

def Clustering(G, N, Ni, k, ListOfKeys):
    for key in ListOfKeys:
        for Node1 in G[key]:
            key0 = Ni[Node1]
            for Node2 in G[key][Node1]:
                key1 = Ni[Node2]
                if key0 == key1:
                    continue
                if len(N) > k:
                    N[key0].extend(N[key1])
                    for i in N[key1]:
                        Ni[i] = key0
                    del N[key1]
                else:
                    return key

def main():
    f_int = open('knapsack1.txt','r')
    param = f.readline().split()
    size = int(param[0])
    numItems = int(param[1])
    length = 0
    listV = dict()
    listW = dict()
    listRV = dict()
    for line in f:
	items = line.split()
	ints = []
        for item in items:
                ints.append(int(item))
        key = tuple(ints)
        if key in listRV:
                listRV[key].append(length)
        else:
                listRV.update({key: [length]})
        listV.update({length: key})
	if ints[0] in listW:
	    if ints[1] not in listW[ints[0]]:
		listW.update({ints[0]: {ints[1]:[]}})
        length += 1	

    idxV = dict()
    for key in listW.keys():
	idxV.update({key: []})
	listW[key].sort()
	for v in listW[key]:
		idxV[key].append(listRV.pop(tuple([key,v])))		

    listK = dict()

    for i in range(size):
	for j in idxV.keys():
		if i < j:
			break
		

    for i in range(numItems):
	for 
    for line in f_int:
        array = line.split()
        array = map(int,array)
        Key = array.pop(2)
        if Key not in G:
            G[Key] = {}
        if array[0] not in G[Key]:
            G[Key][array[0]] = []
        G[Key][array[0]].append(array[1])
    f_int.close()
    ListOfKeys = G.keys()
    ListOfKeys.sort()
    print Clustering(G, N, Ni, k, ListOfKeys)
    print "Press any key to continue"
    raw_input()

main()
