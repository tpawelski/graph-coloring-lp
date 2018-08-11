# Solving the Graph Coloring Problem and Sudoku Application with Linear Programming Algorithms
  
  The graph coloring problem (finding the chromatic number) is a common problem in Management Science with applications including scheduling optimization, timetabling, assignment problems, etc. 
  
__Definition 1:__ A `coloring` of an undirected graph G consists of assigning a number (or a color) to each node, with the restriction that any two nodes that have an edge in between cannot be assigned the same number (or color).

__Definition 2:__ The `chromatic number` of a graph is k ∈ N if there exists a coloring that uses k colors, but there is no coloring that uses less than k colors. Thus, the chromatic number is the minimum number of colors needed to have a coloring of a graph.

The python 3.0 script [GraphColoringLP.py](https://github.com/tpawelski/graph-coloring-lp/blob/master/GraphColoringLP.py), uses the `PuLP` library in python to set up and solve the graph coloring problem as a linear program. The program finds the chromatic number of the graph represented as a list of edges in [edges.dat](https://github.com/tpawelski/graph-coloring-lp/blob/master/edges.dat).
