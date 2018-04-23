import sys
import random

def Schedule(G):
    ListOfKeys = G.keys()
    ListOfKeys.sort()
    ListOfKeys.reverse()    
    WCT = 0
    Time = 0
    for key in ListOfKeys:
        ListOfWeights = G[key].keys()
        ListOfWeights.sort()
        ListOfWeights.reverse()
        for w in ListOfWeights:
            for l in G[key][w]:
                Time += l
                WCT += w*Time
    return WCT

def main():
    f_int = open('jobs.txt','r')
    array = []
    edge = []
    NumberOfJob = (int)(f_int.readline())
    Gdiff = {}
    Gratio = {}
    for line in f_int:
        array = line.split()
        array = map(int,array)
        KeyDiff = array[0] - array[1]
        KeyRatio = float(array[0])/float(array[1])
        if KeyDiff not in Gdiff:
            Gdiff[KeyDiff] = {}
        if KeyRatio not in Gratio:
            Gratio[KeyRatio] = {}
        if array[0] not in Gdiff[KeyDiff]:
            Gdiff[KeyDiff][array[0]] = []
        if array[0] not in Gratio[KeyRatio]:
            Gratio[KeyRatio][array[0]] = []
        Gdiff[KeyDiff][array[0]].append(array[1])
        Gratio[KeyRatio][array[0]].append(array[1])
    f_int.close()
    WCTDiff = Schedule(Gdiff)
    WCTRatio = Schedule(Gratio)
    print WCTDiff
    print WCTRatio
    print "Press any key to continue"
    raw_input()

main()
