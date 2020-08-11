from util import Stack

def earliest_ancestor(ancestors, starting_node): 
    # ancestors is an array of sets: (u, v)
    # trace the graph and make a path until we reach a vertex that has no ancestors
    # if multiple vertices have no ancestors, return the last value of the longer path

    # create a dictionary for storing vertices
    vertices = {}

    # creating a graph of vertices and edges using the ancestors array
    for i in ancestors:
        # use the second element of each set as the key
        if i[1] not in vertices:
            # initialize each value as a set
            vertices[i[1]] = set()
        # add the first element of each set to its corresponding key (edges)
        vertices[i[1]].add(i[0])

    # a function for getting all ancestors of a vertex
    def _get_ancestors(vertex):
        if vertex in vertices.keys():
            return vertices[vertex]
        else:
            return [None]
    
    # create a stack to traverse vertices
    s = Stack()            
    # initialize stack with starting_node in a list (path)   
    s.push([starting_node]) 
    # initialize a visited set to track visited vertices  
    visited = set()           
    # a list to store all possible paths of ancestors
    paths = []                

    # while the stack is not empty
    while s.size() > 0:   
        # pop a path from the top of the stack   
        p = s.pop()       
        # get the last vertex of that path   
        v = p[-1]             

        if v not in visited:
            # mark the vertex as visited
            visited.add(v)    

            # get all ancestors of the vertex
            for ancestor in _get_ancestors(v):  
                # if there are ancestors:
                if ancestor is not None:     
                    # create a copy of the current path   
                    p2 = p.copy()      
                    # add an ancestor to the path         
                    p2.append(ancestor)         
                    # add the path to the stack
                    s.push(p2)      
                # else if there are no ancestors:            
                elif v == starting_node:   
                    # return -1     
                    return -1                   
            # append the path to the list of paths
            paths.append(p)    

    # initialize empty array to find longest path
    last = []                                  

    # iterate through paths to find the longest
    for i in paths:                            
        if len(i) > len(last):
            last = i   
    # return the last element of the longest path
    return last[-1]                            