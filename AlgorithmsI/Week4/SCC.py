import sys
import random

def FinishingTime(NumberOfVertice, Grev):
    Explored = {}
    for i in range(NumberOfVertice):
        Explored[i] = False
    Time = 0
    FinishTime = {}
    TimeStack = []
    KeyQueue = []
    for i in range(NumberOfVertice):
        FinishTime[i] = 0
    for i in range(NumberOfVertice):
        if Explored[i] == False:
            Explored[i] = True
            stack = [i]
            while len(stack) >= 1:
                Key = stack.pop()
                for j in Grev[Key]:
                    if Explored[j] == False:
                        Explored[j] = True
                        stack.append(j)
                KeyQueue.append(Key)
                TimeStack.append(Time)
                Time += 1
#            print TimeStack
            while len(TimeStack) >= 1:
                FinishTime[TimeStack.pop()] = KeyQueue.pop(0)
    return FinishTime
                
def StronglyConnectedComponents(NumberOfVertice, G, FinishTime):
    rev = range(NumberOfVertice)
    rev.reverse()
    Explored = {}
    for i in range(NumberOfVertice):
        Explored[i] = False
    CountConnected = []
    for i in rev:
        k = FinishTime[i]
        if Explored[k] == False:
            Explored[k] = True
            stack = [k]
            Count = 1
            while len(stack) >= 1:
                key = stack.pop()
                for j in G[key]:
                    if Explored[j] == False:
                        Explored[j] = True
                        stack.append(j)
                        Count += 1
            CountConnected.append(Count)
    CountConnected.sort()
    CountConnected.reverse()
    return CountConnected

def main():
    f_int = open('SCC.txt','r')
    array=[]
    NumberOfVertice = 875714
#    NumberOfVertice = 11
    Grev = {}
    for i in range(NumberOfVertice):
        Grev[i]=[]
    for line in f_int:
        array = map(int, line.split())
        key = array.pop(1) - 1
        Grev[key].append(array.pop(0) - 1)
    f_int.close()
    FinishTime = []
    FinishTime = FinishingTime(NumberOfVertice, Grev)
#    print FinishTime
    G = {}
    f_int = open('SCC.txt','r')
    for i in range(NumberOfVertice):
        G[i]=[]
    for line in f_int:
        array = map(int, line.split())
        key = array.pop(0) - 1
        G[key].append(array.pop(0) - 1)
    f_int.close()
    CountConnected = []
    CountConnected = StronglyConnectedComponents(NumberOfVertice, G, FinishTime)
    print CountConnected[0:5]
    print "Press any key to continue"
    raw_input()

# 434821,968,459,313,211

main()
