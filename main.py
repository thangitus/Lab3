from Graph import Graph

g = Graph()
for i in range(7):
    g.addVertex(i)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(3, 2)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(5, 3)
g.addEdge(6, 5)
scc = g.strongly_connected_components()
for community in scc:
    print([v.getId() for v in community])
