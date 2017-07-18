def is_valid(parent, start, end):
    arry = []
    if (start == end or end == None):
        return [start]
    
    else:
        return is_valid(parent,start,parent[end])+ [end]
        
    return arry


def tree_path(parent, start, end): 
    if (parent[start] == None and parent[end] == None):
        return []

    else:
        return is_valid(parent, start, end)
        
    
print(tree_path([None, 0], 0, 1))
print(tree_path([None, 2, 3, None, 3, 4], 3, 5))
print(tree_path([None, 2, 3, None, 3, 4], 3, 0))
print(tree_path([None, 0, 1, 2, 3], 0, 4))
print(tree_path([5, 2, None, 1, 1, 4], 2, 0))
