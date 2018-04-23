import sys
import random

def TwoSum(G):
    count = 0
    for t in range(-10000,10001):
        print t
        for i in G:
            if (t-i) in G:
                count += 1
                break
    return count

def main():
    f_int = open('algo1-programming_prob-2sum.txt','r')
    array = []
    G = {}
    for line in f_int:
        array = line.split()
        key = (int)(array.pop())
        G[key] = key
    f_int.close()
    Count = TwoSum(G)
    print Count
    print "Press any key to continue"
    raw_input()

main()
