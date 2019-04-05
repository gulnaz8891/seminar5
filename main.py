from mygraph import Graph
from myalgorithm import kruskalsalg

with open('graph_17.txt') as f:
    s = f.readline()
    t = []
    for line in f:
        t.append([int(i) for i in line.split()])

cnt = 0
g = Graph()

weight = []
for i in range(len(t)):
    weight.append(t[i][len(t[i]) - 1])

for i in range(len(t[0]) - 1):
    g.add_vertex(i)

for j in range(len(t)):
    x = None
    y = None
    cnt = 0
    for i in range(len(t[0]) - 1):
        if cnt == 0 and t[j][i] == 1:
            x = i
            cnt = 1
            continue
        if t[j][i] == 1 and cnt == 1:
            y = i
            cnt = 2
        if cnt == 2:
            g.add_edge(x, y, weight[j])
            break

g.print_graph()
print('Vertices:', g.vertices())
print('Edges: ', g.edges())
print('num_vertices:', g.num_vertices())
print('num_edges:', g.num_edges())
print('get_vertex: ', g.get_vertex(3))
print('get_edge: ', g.get_edge(2, 3))
print('adj_vertices: ', g.adj_vertices(1))
print('Minimum Spanning Tree:')
print(kruskalsalg(g.get_data(), g.num_vertices()))

#Yermagambet Gylnaz

