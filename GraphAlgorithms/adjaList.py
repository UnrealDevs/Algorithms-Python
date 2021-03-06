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


    
def bfs_tree(adj_list, start):
    d = deque()
    parent = [None for i in range(0,len(adj_list))]
    state = ["undiscovered" for i in range(0,len(adj_list))]
    d.append(start)
    i=0
    while len(d) > 0:
        currentVertex = d.popleft()
        for vertex, weight in adj_list[currentVertex]:
            if state[vertex] == "undiscovered":
               state[vertex] = "discovered"
               parent[vertex] = currentVertex
               d.append(vertex)
        state[currentVertex] = "processed"
        print("Iteration {}: {}, {}".format(i,state, parent))
        i+=1
    return parent




def tree_path_iterative(parent, start, end):
    path = []
    while start!= end and start != None and end!= None:
        path.append(end)
        end = parent[end]
    path.append(start)
    if len(path) == 2 and len(parent) != 2:
        return []
    return [element for element in reversed(path)]
        

def DFS_Visit(adjList, s, state, parent,stack):
    for v,w in adjList[s]:
        if state[v] == "undiscovered":
            state[v] = "discovered"
            parent[v] = s
            print(state,parent)
            DFS_Visit(adjList, v, state,parent,stack)
    stack.append(s)


        
def DFS(adjList, s):
    parent = [None for i in range(0,len(adjList))]
    state = ["undiscovered" for i in range(0,len(adjList))]
    state[s] = "discovered"
    stack = []
    DFS_Visit(adjList, s, state, parent, stack)
    return stack


def dijkstra(graph, start):
    intree = []
    parent = []
    distance = []
    for i in range(0,len(graph)):
        intree.append(False)
        parent.append(None)
        distance.append(float('inf'))
    distance[start] = 0
    current = start
    i=1
    while (intree[current] == False):
        intree[current] = True
        
        for vertex, weight in graph[current]:
            if (distance[vertex] > (distance[current] + weight)):
                distance[vertex] = distance[current] + weight
                parent[vertex] = current
        currentMin = float('inf')
        current = 0
        for v in range(0,len(distance)):
            if (intree[v] == False and distance[v] < currentMin):
                currentMin = distance[v]
                current = v
        
        print("Iteration {}: {}, {}, {}".format(i,distance, intree, parent))
        i+=1
        

def prims(graph, start):
    intree = []
    parent = []
    distance = []

    for i in range(0,len(graph)):
        intree.append(False)
        parent.append(None)
        distance.append(float('inf'))

    distance[start] = 0
    current = start
    i = 0
    while intree[current] == False:
        intree[current] = True
        for vertex, weight in adjList[current]:
            if distance[vertex] > weight and intree[vertex] == False :
                distance[vertex] = weight
                parent[vertex] = current
        
        currentMin = float('inf')
        current = 0
        for v in range(0,len(distance)):
            if (intree[v] == False and distance[v] < currentMin):
                currentMin = distance[v]
                current = v
        
        print("Iteration {}: {}, {}, {}".format(i,distance, intree, parent))
        i+=1


def floyds(adjList):
    pass

def dfsVisit(vertex, adjList, processed, stack):
    for v,w in adjList[vertex]:
        if processed[v] == False:
            dfsVisit(v,adjList,processed,stack)
    processed[vertex] = True
    stack.append(vertex)

    
def dfsTop(adjList):
    processed = [False for k in adjList]
    stack = []
    for i in range(0,len(adjList)):
        if processed[i] != True:
            dfsVisit(i, adjList, processed, stack)
    
    return stack
    
    
graph_str = """\
U 6
1 2
3 4
5 4
3 5
"""
adjList = adjacency_list(graph_str)
bfs_tree(adjList,5)
