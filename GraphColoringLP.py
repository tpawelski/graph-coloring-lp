from pulp import *

#file containint the list of edges in graph G
edge_list = open("/Users/tommypawelski/Downloads/edges.dat")

#creates a 30x30 nested list of 0's to make adjacency matrix for graph G
list0 =[]
for i in range(0,30):
    list0.append([0]*30)

#reads in data from edges file and stores edges in list of tuples
data=''
for line in edge_list.readlines():
    data += line
data=eval(data)
edge_list.close()

#adjacency matrix value at [r][c] set equal to 1 if edge between r and c
for tup in data:
    r=tup[0]
    c=tup[1]
    list0[r][c] = 1
    list0[c][r]= 1

n=10
nodes = range(30)
y=range(n)
#initializes lp problem
lp = LpProblem("Coloring Problem",LpMinimize)
# The problem variables are created
# variables x_ij to indicate whether node i is colored by color j;
xij = LpVariable.dicts("x",(nodes,y),0,1,LpInteger)
#variables yj to indicate whether color j was used
yj = LpVariable.dicts("y",y,0,1,LpInteger)

#objective is the sum of yj over all j
obj = lpSum(yj[j] for j in y)
lp += obj, "Objective Function"

#constraint s.t. each node uses exactly 1 color
for r in nodes:
    jsum=0.0
    for j in y:
        jsum += xij[r][j]
    lp += jsum==1,""

#constraint s.t. adjacent nodes do not have the same color
for row in range(0,len(list0)):
    for col in range(0, len(list0)):
        if list0[row][col]==1:
            for j in y:
                lp += xij[row][j] + xij[col][j] <= 1,""

#constraint s.t. if node i is assigned color k, color k is used
for i in nodes:
    for j in y:
        lp += xij[i][j]<=yj[j],""

#constrinat for upper bound on # of colors used
lp += lpSum(yj[j] for j in y)<= n,""

#solves lp and prints optimal solution/objective value
lp.solve()
status = str(LpStatus[lp.status])
print("Solution: "+ status)

print("Optimal Solution:")
print("Xij=1 values:")
for i in nodes:
	for j in y:
		if xij[i][j].value() == 1:
		          print(xij[i][j])

print("Yj values:")
for j in y:
    print(yj[j], yj[j].value())
print("Chromatic Number: ", value(lp.objective))
