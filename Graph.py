from Vertex import Vertex


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key) -> Vertex:
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, weight=0):
        u, v = self.getVertex(f), self.getVertex(t)
        if f not in self.vertList:
            u = self.addVertex(f)
        if t not in self.vertList:
            v = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)
        return u, v

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def dfs(self, u: Vertex, visited, comp):
        visited.add(u)
        comp.append(u)
        for v in u.getConnections():
            if v not in visited:
                self.dfs(v, visited, comp)

    def get_transpose(self):
        gt = Graph()
        for vertex in self:
            gt.addVertex(vertex.getId())
        for vertex in self:
            for neighbor in vertex.getConnections():
                gt.addEdge(neighbor.getId(), vertex.getId(), vertex.getWeight(neighbor))
        return gt

    def dfs_order(self, u, stack, visited):
        visited.add(u)
        for v in u.getConnections():
            if v not in visited:
                self.dfs_order(v, stack, visited)
        stack.append(u)

    def strongly_connected_components(self):
        stack = []
        visited = set()
        for u in self:
            if u not in visited:
                self.dfs_order(u, stack, visited)
        gt = self.get_transpose()
        visited = set()
        scc = []
        while stack:
            u = gt.getVertex(stack.pop().getId())
            if u not in visited:
                component = []
                gt.dfs(u, visited, component)
                scc.append(component)
        return scc
