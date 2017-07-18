def adjacency_list(graph_str):
    """Converts str graph rep to adj list"""
    lines = graph_str.splitlines()
    other = []
    for line in lines:
        other.append(line.split())
    
    adjList = [[] for _ in range(int(other[0][1]))]
    info = other[:1]
    list1 = other[1:]
   

    if (info[0][0] == "D"):
        
        for i in range(0,len(list1)): 
            if len(info[0]) == 2:
                adjList[int(list1[i][0])].append((int(list1[i][1]),None))
            else:
                adjList[int(list1[i][0])].append((int(list1[i][1]),int(list1[i][2])))
                 
                   
    else:
        for i in range(0,len(list1)): 
            if len(info[0]) == 2:
                adjList[int(list1[i][0])].append((int(list1[i][1]),None))
                adjList[int(list1[i][1])].append((int(list1[i][0]),None))
                
            else:
                adjList[int(list1[i][0])].append((int(list1[i][1]),int(list1[i][2])))
                adjList[int(list1[i][1])].append((int(list1[i][0]),int(list1[i][2])))
        
    return adjList


def prims(adjList, start):

    parent = [None for _ in adjList]
    distance = [float('inf') for _ in adjList]
    intree = [False for _ in adjList]

    distance[start] = 0

    v = start

    while (intree[v] == False):

        intree[v] = True
        adjVertices = adjList[v] # all adj vertices to V


        for (vertex, weight) in adjVertices:
            
            
    print(parent,distance)
        
    


graph_string = """\
U 7 W
1 2 2
1 5 4
1 6 6
2 3 3
2 5 9
3 4 5
4 5 3
"""
adjList = adjacency_list(graph_string)


prims(adjList,0)
