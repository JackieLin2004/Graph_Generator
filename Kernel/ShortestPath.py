import math
import networkx as nx
from collections import deque


# 手动实现FLOYD算法
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

    # 原生库实现的floyd算法，用以做比较
    @staticmethod
    def lib_Floyd_Algorithm(graph):
        # G = None
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


# 手动实现SPFA算法
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
                if matrix[i][j] != 0 and i != j:
                    g[i].append([j, matrix[i][j]])

        path = [-1] * n
        INF = math.inf
        dis = [INF] * n
        q = deque()
        vis = [False] * n
        cnt = [0] * n

        dis[st] = 0
        q.append(st)
        vis[st] = True
        cnt[st] = 1
        # 判断负环
        flag = True

        while q:
            u = q.popleft()
            vis[u] = False
            for v, w in g[u]:
                if dis[v] > dis[u] + w:
                    dis[v] = dis[u] + w
                    if not vis[v]:
                        cnt[v] += 1
                        q.append(v)
                        vis[v] = True
                        path[v] = u
                        if cnt[v] >= n - 1:
                            flag = False
                            break
            if not flag:
                break

        if dis[ed] == INF:
            return 0, None
        elif not flag:
            return 1, None
        else:
            self.search_path(path, ed)
            return 2, self.Tpath

    def search_path(self, path, end):
        if path[end] == -1:
            self.Tpath.append(end)
            return
        self.search_path(path, path[end])
        self.Tpath.append(end)

    # 原生库实现的bellman-ford算法，用以做比较
    @staticmethod
    def lib_Bellman_Ford_Algorithm(graph, st, ed):
        st = int(st)
        ed = int(ed)
        # G = None
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
