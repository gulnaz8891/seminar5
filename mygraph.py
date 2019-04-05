class Graph(object):

    def __init__(self, _graph=None):
        if _graph == None:
            _graph = {}
        self._graph = _graph
        self.graphdata = []
        
    def print_graph(self):
        for v in self._graph.keys():
            print(v, ":", self._graph[v])
        return self._graph

    def num_vertices(self):
        return len(list(self._graph.keys()))

    def num_edges(self):
        return len(self.edges())

    def add_vertex(self, vertex):
        if vertex not in self._graph.keys():
            self._graph[vertex] = []

    def add_edge(self,u,v,w):
        if v not in self._graph[u]:
            self._graph[u].append(v)
        if u not in self._graph[v]:
            self._graph[v].append(u)
        self.graphdata.append([u,v,w])
        
    def get_vertex(self, v):
        if v in self._graph:
            return self._graph[v]
        else:
            return None
    def get_edge(self, u, v):
        try:
            if u in self._graph[v] or v in self._graph[u]:
                exists = '(' + str(u) + ', ' +  str(v) + ') exist'
                return exists
        except:
            return "(" + str(u) + ', ' +  str(v) + ") does not exist"

    def get_data(self):
        return self.graphdata
    def vertices(self):
        return list(self._graph.keys())

    def edges(self):
        edges = []
        for vertex in self._graph.keys():
            for neighbour in self._graph[vertex]:
                if (neighbour, vertex) not in edges:
                    edges.append((vertex, neighbour))
        return edges

    def adj_vertices(self, v):
        s = list(self._graph[v])
        res = []
        for k in self._graph.keys():
            if v in self._graph[k]:
                res.append(k)
        for p in s:
            if p not in res:
                res.append(p)
        return res
