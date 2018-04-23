import sys
import random

def CountEdge(NumberOfVertice, ListsOfVertices, CountedEdge):
    for i in range(NumberOfVertice):
        CountedEdge.append(len(ListsOfVertices[i]) + CountedEdge[i])

def FindEdge(RandEdge, CountEdge, MinVert, MaxVert):
    if (MaxVert - MinVert) == 1:
        i = MinVert
        j = RandEdge - CountEdge[MinVert] - 1
    elif RandEdge < CountEdge[(MinVert + MaxVert)/2]:
        i,j = FindEdge(RandEdge, CountEdge, MinVert, (MaxVert + MinVert)/2 )
    elif RandEdge > CountEdge[(MinVert + MaxVert)/2]:
        i,j = FindEdge(RandEdge, CountEdge, (MinVert + MaxVert)/2, MaxVert)
    else:
        i = (MinVert + MaxVert)/2
        j = RandEdge - CountEdge[(MinVert + MaxVert)/2] - 1
    return (i, j)

def Contraction(IndexOfVertice, ListsOfVertices, i, j):
    VerticeB = ListsOfVertices[i][j]
    IndexB = IndexOfVertice.index(VerticeB)
    if IndexB < i + 1:
        IndexA = IndexB
        IndexB = i
    else:
        IndexA = i
    VerticeA = IndexOfVertice[IndexA]
    VerticeB = IndexOfVertice[IndexB]
    for v in ListsOfVertices[IndexB]:
        IndexV = IndexOfVertice.index(v)
        cnt = ListsOfVertices[IndexV].count(VerticeB)
        for c in range(cnt):
            ListsOfVertices[IndexV].remove(VerticeB)
            ListsOfVertices[IndexV].append(VerticeA)
        ListsOfVertices[IndexV].sort()
    ListsOfVertices[IndexA].extend(ListsOfVertices.pop(IndexB))
    cnt = ListsOfVertices[IndexA].count(VerticeA)
    for c in range(cnt):
        ListsOfVertices[IndexA].remove(VerticeA)
    IndexOfVertice.pop(IndexB)

def MinCut(ListOfCut):
    f_int=open('kargerMinCut.txt','r')
#    f_int=open('MinCut.txt','r')
#    f_int=open('test1.txt','r')
    array=[]
    NumberOfVertice = 200
    IndexOfVertice =[]
    ListsOfVertices = [[] for i in range(NumberOfVertice)]
    for line in f_int:
        array = line.split()
        Index = array.pop(0)
        IndexOfVertice.append(Index)
        ListsOfVertices[int(Index)-1] = array
    while  NumberOfVertice > 2:
        CountedEdge = [0]
        CountEdge(NumberOfVertice, ListsOfVertices, CountedEdge)
        RandEdge = random.randint(1,CountedEdge[NumberOfVertice])
        i,j = FindEdge(RandEdge, CountedEdge, 0, NumberOfVertice)
        Contraction(IndexOfVertice, ListsOfVertices, i, j)
        NumberOfVertice = len(IndexOfVertice)
    if len(ListsOfVertices[0]) == len(ListsOfVertices[1]):
        ListOfCut.append(len(ListsOfVertices[0]))
    else:
        print 'Contraction Failure :('

def main():
    ListOfCut = []
    for i in range(1,500000):
        print i
        MinCut(ListOfCut)
    print 'Maximum of cut', max(ListOfCut)
    print 'Minimum of cut', min(ListOfCut)
    print "Press any key to continue"
    raw_input()

   
    f_int.close()

main()
