def find(parent, n): 
    if parent[n] == n: 
        return n 
    return find(parent, parent[n]) 

def union(parent, rank, x, y): 
    xroot = find(parent, x) 
    yroot = find(parent, y) 

    if rank[xroot] < rank[yroot]: 
        parent[xroot] = yroot 
    elif rank[xroot] > rank[yroot]: 
        parent[yroot] = xroot 

    else : 
        parent[yroot] = xroot 
        rank[xroot] += 1

def kruskalsalg(graph, V):
    res = []
    i = 0
    e = 0
    parent = []
    rank = []
    graph = sorted(graph, key = lambda item: item[2]) 
    
    for v in range(V):
        parent.append(v)
        rank.append(0)

    while e < V -1 : 
        u,v,w =  graph[i] 
        i += 1
        x = find(parent, u) 
        y = find(parent ,v) 
  
        if x != y: 
            e = e + 1     
            res.append([u,v,w]) 
            union(parent, rank, x, y) 

    return res            
