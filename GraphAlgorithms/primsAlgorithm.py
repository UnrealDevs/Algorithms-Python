from collections import deque

def adjacency_list(graph_str):
    graph = graph_str.splitlines()
    array = [line.split() for line in graph]
    graph_info = array[0]
    adjList = [[] for i in range(0,int(graph_info[1]))]
    if len(graph_info) < 3:
        for i in range(0,len(array)):
            array[i].append(None)
    for v1,v2,weight in array[1:]:
        if weight != None:
            weight = int(weight)
        if graph_info[0] == "D":
            adjList[int(v1)].append((int(v2), weight))
        else:
            adjList[int(v1)].append((int(v2), weight))
            adjList[int(v2)].append((int(v1), weight))     
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
