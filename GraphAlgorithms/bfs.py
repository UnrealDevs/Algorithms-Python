from collections import deque
def bfs_tree(adj_list, start):
    """BFS"""
    d = deque()
    ########initialisation of states/parents#########
    state = [[] for _ in adj_list]
    parent = [[] for _ in adj_list]

    
    for i in range(0,len(adj_list)):
        state[i] = "undiscovered"
        parent[i] = None


    #################################################
    state[start] = "discovered"  #set state/parent of the starting vertex
    parent[start] = None


    d.append(start) #enqueue the starting vertex


    while (len(d) > 0):
        currentVertex = d.popleft() #pop from left side
    
        for i in range(0,len(adj_list[currentVertex])): # through all adj vertices
            
            if state[adj_list[currentVertex][i][0]] == "undiscovered":
                state[int(adj_list[currentVertex][i][0])] = "discovered" #discover all vertices adj to current
                parent[adj_list[currentVertex][i][0]] = currentVertex # set parent to current vertex
                d.append(int(adj_list[currentVertex][i][0])) # enqueue right of deque
        state[int(currentVertex)] = "processed" #mark as processed

    return parent
