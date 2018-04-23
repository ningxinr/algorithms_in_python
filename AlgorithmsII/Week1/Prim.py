import sys
import random

def Schedule(G):
    ListOfKeys = G.keys()
    ListOfKeys.sort()
    ListOfKeys.reverse()    
    WCT = 0
    Time = 0
    cnt = 0
    for key in ListOfKeys:
        ListOfWeights = G[key].keys()
        ListOfWeights.sort()
        ListOfWeights.reverse()
        for w in ListOfWeights:
            for l in G[key][w]:
                Time += l
                WCT += w*Time
                cnt += 1
    print cnt
    return WCT

def main():
    f_int = open('edges.txt','r')
    array = []
    edge = []
    array = map(int,f_int.readline())
    NumberOfNodes = array.pop()
    NumberOfEdges = array.pop()
    G = {}
    for line in f_int:
        array = line.split()
        array = map(int,array)
        
    f_int.close()
    WCTDiff = Schedule(Gdiff)
    WCTRatio = Schedule(Gratio)
    print WCTDiff
    print WCTRatio
    print "Press any key to continue"
    raw_input()

main()
