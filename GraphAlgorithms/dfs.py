def DFS_Visit(adjList, s, state, parent):
    for v,w in adjList[s]:
        if state[v] == "undiscovered":
            state[v] = "discovered"
            parent[v] = s
            DFS_Visit(adjList, v, state,parent)
         
        state[v] = "processed"

        
def DFS(adjList, s):
    parent = [None for i in range(0,len(adj_list))]
    state = ["undiscovered" for i in range(0,len(adj_list))]
    state[s] = "discovered"
    DFS_Visit(adjList, s, state, parent)
    return parent


adj_list = [
    [(1, None)],
    [(0, None), (2, None)],
    [(1, None)]
]

print(DFS(adj_list, 0))

