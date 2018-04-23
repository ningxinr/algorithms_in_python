import sys
import random

def Dijkstra(NumberOfVertice, G):
    X = {}
    X[0] = 0
    while len(X) < NumberOfVertice:
        Min = 100000000
        for i in X:
            for edge in G[i]:
                if (edge[0] - 1) not in X:
                    if (X[i] + edge[1]) <= Min:
                        Min = X[i] + edge[1]
                        key = edge[0] - 1
        X[key] = Min
    return X

def main():
    f_int = open('dijkstraData.txt','r')
    array = []
    edge = []
    NumberOfVertice = 200
    G = {}
    for i in range(NumberOfVertice):
        G[i]=[]
    for line in f_int:
        array = line.split()
        key = (int)(array.pop(0)) - 1
        for i in range(len(array)):
            edge = array[i].split(',')
            G[key].append(map(int,edge))
    f_int.close()
    ShortestPath = Dijkstra(NumberOfVertice, G)
    print ShortestPath[6]
    print ShortestPath[36]
    print ShortestPath[58]
    print ShortestPath[81]
    print ShortestPath[98]
    print ShortestPath[114]
    print ShortestPath[132]
    print ShortestPath[164]
    print ShortestPath[187]
    print ShortestPath[196]
    print "Press any key to continue"
    raw_input()

main()
