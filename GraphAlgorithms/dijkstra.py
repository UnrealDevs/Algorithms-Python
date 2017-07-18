def dijkstra_tree(adj_list, start):
    distance = [float('inf') for v in adj_list]
    intree = [False for v in adj_list]
    parent = [None for v in adj_list]
    
    
    distance[start] = 0
    
    
    current = start
    
    while intree[current] == False:
        intree[current] = True
        
        for vertex, weight in adj_list[current]:
            if distance[vertex] > distance[current] + weight:
                parent[vertex] = current
                distance[vertex] = distance[current] + weight
                
       
        dist = float('inf')
        for i in range(0, len(distance)):
            if (intree[i] == False and (dist > distance[i])):
                dist = distance[i]
                current = i
                
    return parent
