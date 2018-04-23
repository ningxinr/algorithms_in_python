listV = [0.05, 0.4, 0.08, 0.04, 0.1, 0.1, 0.23]
optBst = []
for i in range(len(listV)+2):
    optBst.append([0]*9)

for i in range(1, len(listV)+1):
    for j in range(1, len(listV)+1):
	if i <= j:
#	    optBst[i][j] = optBst[i-1][j]
	    print optBst[0]    
	    print optBst[1]    
	    print optBst[2]    
	    print optBst[3]    
	    print optBst[4]    
	    print optBst[5]    
	    print optBst[6]    
	    print optBst[7]    
	    tmp = listV[i-1]
            for l in range(i, j+1):
	    	print "i: ", i, "j: ", j, "l: ", l
	        optBst[i][j] = min(optBst[i][j], optBst[i][l-1] + optBst[l+1][j])
		tmp += listV[l-1]
		print optBst[0]    
		print optBst[1]    
		print optBst[2]    
		print optBst[3]    
		print optBst[4]    
		print optBst[5]    
		print optBst[6]    
		print optBst[7]    
	    # optBst[i][i+s] = min(optBst[i][i+s], optBst[i+1][i+s])
	    optBst[i][j] += tmp
print optBst[0]    
print optBst[1]    
print optBst[2]    
print optBst[3]    
print optBst[4]    
print optBst[5]    
print optBst[6]    
print optBst[7]    
print "result: ", optBst[1][7]
