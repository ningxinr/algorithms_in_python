from decimal import *

f = open("g0.txt",'r')
params = f.readline().split()
numV = int(params[0])
numE = int(params[1])
g = dict()
a = dict()

for line in f:
    edge = line.split()
    pairV = tuple([int(edge[0])-1, int(edge[1])-1])
    if pairV in g:
	g[pairV].append(int(edge[2]))
    else:
	g.update({pairV: int(edge[2])})

A = [[[0 for i in range(2)] for j in range(numV)] for k in range(numV)]

for i in range(numV):
    for j in range(numV):
	pairV = tuple([i, j])
	if i == j:
	    A[i][j][0] = 0
	elif pairV in g:
	    A[i][j][0] = g[pairV] 
	else:
	    A[i][j][0] = Decimal("Infinity")

minPath = Decimal("Infinity")

for k in range(1, numV+1):
    for i in range(numV):
	for j in range(numV): 
	    A[i][j][k%2] = min(A[i][j][(k-1)%2], A[i][k-1][(k-1)%2] + A[k-1][j][(k-1)%2])
	    print "i: ", i, "j: ", j, "k: ", k, "Aijk: ", A[i][j][k%2]

for i in range(numV):
    for j in range(numV):
	    minPath = min(minPath, A[i][j][numV%2])

for i in range(numV):
    if A[i][i][numV%2] < 0:
	minPath = Decimal("NaN")

print minPath
