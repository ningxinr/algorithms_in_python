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
    f_int = open('clustering1.txt','r')
    array = []
    NumberOfNode = (int)(f_int.readline())
    k = 4
    G = {}
    N = {}
    Ni = {}
    for i in range(1, NumberOfNode+1):
        N[i] = [i]
        Ni[i] = i
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
