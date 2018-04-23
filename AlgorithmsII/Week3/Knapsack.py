import sys
import math

def main():
    f = open('knapsack_big.txt','r')
    param = f.readline().split()
    size = int(param[0])
    numItems = int(param[1])
    length = 0
    listV = dict()
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
        length += 1	

    K = []
    K.append(range(size+1))
    K.append(range(size+1))
    for i in range(numItems):
	for j in range(size+1):
		if i == 0 :
			K[i%2][j] = 0
		elif j < listV[i][1]:
			K[i%2][j] = K[(i-1)%2][j]
		else:
			K[i%2][j] = max(K[(i-1)%2][j], K[(i-1)%2][j-listV[i][1]] + listV[i][0])	
    print "result: ", K[(numItems-1)%2][size]
    print "Press any key to continue"
    raw_input()

main()
