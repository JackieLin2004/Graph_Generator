import math
import networkx as nx
from collections import deque


class Floyd:
    def __init__(self):
        self.dist = None

    def work(self, graph):
        self.dist = [[math.inf for _ in range(graph.MAX_NODE_SIZES + 1)] for _ in range(graph.MAX_NODE_SIZES + 1)]
        for i in range(1, graph.MAX_NODE_SIZES + 1):
            for j in range(1, graph.MAX_NODE_SIZES + 1):
                if i == j:
                    self.dist[i][j] = 0

        for u, v, w in graph.edges_buffer:
            self.dist[u][v] = min(self.dist[u][v], w)

        for k in range(1, graph.MAX_NODE_SIZES + 1):
            for i in range(1, graph.MAX_NODE_SIZES + 1):
                for j in range(1, graph.MAX_NODE_SIZES + 1):
                    self.dist[i][j] = min(self.dist[i][j], self.dist[i][k] + self.dist[k][j])

        return self.dist

    def lib_Floyd_Algorithm(self, graph):
        G = None
        if graph.Gtype == 0:
            G = nx.Graph()
        else:
            G = nx.DiGraph()
        G.add_nodes_from(range(1, graph.MAX_NODE_SIZES + 1))
        n = len(graph.matrix)
        for i in range(1, n):
            for j in range(1, n):
                if graph.matrix[i][j] != 0:
                    G.add_edge(i, j, weight=graph.matrix[i][j])
        fwPath = nx.floyd_warshall(G)
        return fwPath


class SPFA:
    # 是bellman-ford算法的队列优化
    def __init__(self):
        self.Tpath = []

    def work(self, matrix, st, ed):
        st = int(st)
        ed = int(ed)
        n = len(matrix)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            for j in range(1, n):
                if matrix[i][j] != 0:
                    t = matrix[i][j]
                    g[i].append([j, t])
        path = [-1] * n  # Added path array with initial value -1
        INF = 0x3f3f3f3f
        dist = [INF] * n
        dist[st] = 0
        vis = [False] * n
        q = deque([st])
        vis[st] = True

        while q:
            t = q.popleft()
            vis[t] = False
            for y, w in g[t]:  # Directly unpacking the tuple
                if dist[y] > dist[t] + w:
                    dist[y] = dist[t] + w
                    path[y] = t  # Storing the predecessor of y
                    if not vis[y]:
                        vis[y] = True
                        q.append(y)

        if dist[ed] == INF:
            print('impossible')
            return None
        else:
            self.search_path(path, ed)
            return self.Tpath

    def search_path(self, path, end):
        if path[end] == -1:  # If there's no predecessor, it's the start node
            self.Tpath.append(end)
            return
        self.search_path(path, path[end])  # Recursively print predecessors
        self.Tpath.append(end)

    def lib_Bellman_Ford_Algorithm(self, graph, st, ed):
        st = int(st)
        ed = int(ed)
        G = None
        if graph.Gtype == 0:
            G = nx.Graph()
        else:
            G = nx.DiGraph()
        G.add_nodes_from(range(1, graph.MAX_NODE_SIZES + 1))
        n = len(graph.matrix)
        for i in range(1, n):
            for j in range(1, n):
                if graph.matrix[i][j] != 0:
                    G.add_edge(i, j, weight=graph.matrix[i][j])
        bfPath = nx.bellman_ford_path(G, st, ed)
        return bfPath
