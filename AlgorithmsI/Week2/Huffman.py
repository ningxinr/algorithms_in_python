import sys
import random

def Clustering(G, N, Ni, NumberOfNodes, NumberOfBits):
    for i in range(1, NumberOfNodes+1):
        for j in range(i+1, NumberOfNodes+1):
            key0 = Ni[i]
            key1 = Ni[j]
            if key0 == key1:
                continue
            Hamming = 0
            for b in range(NumberOfBits):
                if G[i][b] ^ G[j][b] :
                    Hamming += 1
                if Hamming > 2:
                    break
            if Hamming < 3:
                N[key0].extend(N[key1])
                for n in N[key1]:
                    Ni[n] = key0
                del N[key1]

def main():
    f_int = open('clustering_small.txt','r')
    array = f_int.readline()
    array = array.split()
    array = map(int, array)
    NumberOfNodes = array[0]
    NumberOfBits = array[1]
    G = {}
    N = {}
    Ni = {}
    for i in range(1, NumberOfNodes+1):
        N[i] = [i]
        Ni[i] = i
    i = 1
    for line in f_int:
        array = line.split()
        array = map(int, array)
        G[i] = array
        i += 1
    f_int.close()
    Clustering(G, N, Ni, NumberOfNodes, NumberOfBits)
    print len(N)
    print "Press any key to continue"
    raw_input()

main()
