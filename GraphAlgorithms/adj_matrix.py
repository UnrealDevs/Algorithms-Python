def adjacency_matrix(graph_str):
    lines = graph_str.splitlines()
    other = []
    for line in lines:
        other.append(line.split())
    numberVer = int(other[0][1])
    adjmatrix = [[] for _ in range(numberVer)]
    for i in range(0,len(adjmatrix)):
        for j in range(0,len(adjmatrix)):
            if (i == j):
                adjmatrix[i].append(0)
            else:
                adjmatrix[j].append("")      
    info = other[:1]
    list1 = other[1:]

    
    if (info[0][0] == "U"):
        for start, end, weight in list1:
            adjmatrix[int(start)][int(end)] = int(weight)
            adjmatrix[int(end)][int(start)] = int(weight)
    else:
        for start, end, weight in list1:
            adjmatrix[int(start)][int(end)] = int(weight)

    
    for i in range(0,len(adjmatrix)):
        for j in range(0,len(adjmatrix)):
            if (adjmatrix[i][j] == ""):
                adjmatrix[i][j] = float("inf")
    return adjmatrix
    
    
    
graph_str = """\
U 3 W
0 1 5
2 1 7
"""

print(adjacency_matrix(graph_str))

graph_str = """\
D 2 W
0 1 4
"""

print(adjacency_matrix(graph_str))
