import sys
import random

def HeapMinInsert(Hmin, n):
    Hmin.append(n)
    i = Hmin.index(n)
    while (i+1)/2-1>=0 and Hmin[(i+1)/2-1] > n:
        temp = Hmin[(i+1)/2-1]
        Hmin[(i+1)/2-1] = n
        Hmin[i] = temp
        i = (i+1)/2-1

def HeapMinExtract(Hmin):
    nmin = Hmin[0]
    Hmin[0] = Hmin.pop(len(Hmin)-1)
    i = 0
    while (i*2+1) < len(Hmin) and (i*2+2) < len(Hmin) and Hmin[i] > min(Hmin[(i+1)*2-1], Hmin[i*2+2]):
        if Hmin[i*2+1] < Hmin[i*2+2]:
            temp = Hmin[i*2+1]
            Hmin[i*2+1] = Hmin[i]
            Hmin[i] = temp
            i = i*2+1
        else:
            temp = Hmin[i*2+2]
            Hmin[i*2+2] = Hmin[i]
            Hmin[i] = temp
            i = i*2+2
    return nmin

def HeapMaxInsert(Hmax, n):
    Hmax.append(n)
    i = Hmax.index(n)
    while (i+1)/2-1>=0 and Hmax[(i+1)/2-1] < n:
        temp = Hmax[(i+1)/2-1]
        Hmax[(i+1)/2-1] = n
        Hmax[i] = temp
        i = (i+1)/2-1

def HeapMaxExtract(Hmax):
    nmax = Hmax[0]
    Hmax[0] = Hmax.pop(len(Hmax)-1)
    i = 0
    while (i*2+1) < len(Hmax) and (i*2+2) < len(Hmax) and Hmax[i] < max(Hmax[(i+1)*2-1], Hmax[i*2+2]):
        if Hmax[i*2+1] > Hmax[i*2+2]:
            temp = Hmax[i*2+1]
            Hmax[i*2+1] = Hmax[i]
            Hmax[i] = temp
            i = i*2+1
        else:
            temp = Hmax[i*2+2]
            Hmax[i*2+2] = Hmax[i]
            Hmax[i] = temp
            i = i*2+2
    return nmax

def MedianMaintenance(N):
    count = 0
    Hmin = []
    Hmax = []
    for i in range(len(N)):
        if len(Hmax)==0 or N[i] < Hmax[0]:
            HeapMaxInsert(Hmax, N[i])
            while len(Hmax) > (len(Hmin)+1):
                nmax = HeapMaxExtract(Hmax)
                HeapMinInsert(Hmin, nmax)
        elif len(Hmin)==0 or N[i] > Hmax[0]:
            HeapMinInsert(Hmin, N[i])
            while len(Hmin) > (len(Hmax)+1):
                nmin = HeapMinExtract(Hmin)
                HeapMaxInsert(Hmax, nmin)
        if len(Hmax) == len(Hmin) or (len(Hmin)+1)==len(Hmax):
            nmed = Hmax[0]
        elif len(Hmax)+1 == len(Hmin):
            nmed = Hmin[0]
        count += nmed
    return count%10000

def main():
    f_int = open('Median.txt','r')
    array = []
    N = []
    for line in f_int:
        array = line.split()
        N.append((int)(array.pop()))
    f_int.close()
    Count = MedianMaintenance(N)
    print Count
    print "Press any key to continue"
    raw_input()

main()
