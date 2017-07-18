def next_vertex(distance_array, in_tree):
    currentMin = float('inf')
    nextVertex = 0
    for v in range(0,len(distance_array)):
        if (in_tree[v] == False and distance_array[v] < currentMin):
            currentMin = distance_array[v]
            nextVertex = v
    return nextVertex
    


distance =   [float('inf'), 0, 3, 12, 5]
in_tree = [False, True, True, False, False]
print(next_vertex(distance, in_tree))
