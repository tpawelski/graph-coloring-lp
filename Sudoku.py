from pulp import *
#creates a nested list of tuples with each [r][c] index representing
#the coordinate location of each box in the sudoku puzzle
index_list=[]
for r in range(1, 10):
    list = []
    for c in range(1,10):
        index = (r,c)
        list.append(index)
    index_list.append(list)

#creates 9 lists of "boxes". Each list containing the coordinates of all squares in each of the 9 boxes
box_list=[]
for r in range(0,3):
    for c in range(0,3):
        box = [index_list[3*r+i][3*c+j] for i in range(0,3) for j in range(0,3)]
        box_list.append(box)

#initialize lp
lp = LpProblem("Sudoku LP",LpMinimize)

#initialize # of rows and columns in puzzle, and # of "colors"
rows = range(1,10)
columns = range(1,10)
numbers = range(1,10)

#initialize the x and y variables
#x is 3 dimensional with row and column (representing location in puzzle), and numbers (1-9 "colors")
#y is 1 dimensional array of "colors" (numbers 1-9)
x_rcj = LpVariable.dicts("x",(rows,columns,numbers),0,1,LpInteger)
yj = LpVariable.dicts("yj",numbers,0,1,LpInteger)

#objective: sum of y over all j
obj=lpSum(yj[j] for j in numbers)
lp += obj, "Objective Function"

#constaint s.t. if node i is assigned color k, color k is used
for r in rows:
    for c in columns:
        for j in numbers:
            lp += x_rcj[r][c][j]<= yj[j],""

# constraint s.t. each node uses exactly one color
for r in rows:
    for c in columns:
        lp += lpSum([x_rcj[r][c][j] for j in numbers]) == 1,""

#constraint s.t. no nodes in the same box have the same number
for j in numbers:
    for box in box_list:
        lp += lpSum([x_rcj[r][c][j] for (r,c) in box]) <= 1,""

#constraint s.t. no nodes in the same row have the same number
for j in numbers:
    for r in rows:
        lp += lpSum([x_rcj[r][c][j] for c in columns]) <= 1,""

#constraint s.t. no nodes in the same column have the same number
for j in numbers:
    for c in columns:
        lp += lpSum([x_rcj[r][c][j] for r in rows]) <= 1,""

#constraint s.t. ALL 9 numbers are used
lp += lpSum(yj[j] for j in numbers)== 9,""

#constraints for pre-filled boxes given in puzzle
lp += x_rcj[1][2][9] == 1,""
lp += x_rcj[1][5][2] == 1,""
lp += x_rcj[1][6][4] == 1,""
lp += x_rcj[1][8][3] == 1,""
lp += x_rcj[2][3][6] == 1,""
lp += x_rcj[2][4][3] == 1,""
lp += x_rcj[2][7][8] == 1,""
lp += x_rcj[3][4][8] == 1,""
lp += x_rcj[3][5][1] == 1,""
lp += x_rcj[3][9][6] == 1,""
lp += x_rcj[4][3][7] == 1,""
lp += x_rcj[4][7][9] == 1,""
lp += x_rcj[4][8][8] == 1,""
lp += x_rcj[5][5][7] == 1,""
lp += x_rcj[6][2][4] == 1,""
lp += x_rcj[6][3][1] == 1,""
lp += x_rcj[6][7][5] == 1,""
lp += x_rcj[7][1][6] == 1,""
lp += x_rcj[7][5][8] == 1,""
lp += x_rcj[7][6][2] == 1,""
lp += x_rcj[8][3][8] == 1,""
lp += x_rcj[8][6][6] == 1,""
lp += x_rcj[8][7][3] == 1,""
lp += x_rcj[9][2][1] == 1,""
lp += x_rcj[9][4][5] == 1,""
lp += x_rcj[9][5][4] == 1,""
lp += x_rcj[9][8][2] == 1,""

#solves lp
lp.solve()
status = str(LpStatus[lp.status])
print("Solution: "+ status)

#prints out optimal solution if one is found
if status == "Optimal":
    for r in rows:
        line=""
        if r in [1,4,7]: print("+=======+=======+=======+")
        for c in columns:
            for j in numbers:
                if value(x_rcj[r][c][j])==1:
                    if c in [1,4,7]: line+="| "
                    line += str(j)+" "
                    if c == 9: line+="| "
        print(line)
    print("+=======+=======+=======+")
else:
    print("Optimal Solution could not be found.")
