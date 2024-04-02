import networkx as nx

# 创建一个有向图
G = nx.DiGraph()
# G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 1), (4, 1)])
# G.add_edges_from([(1, 2), (3, 2)])
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 1), (3, 4), (4, 1)])

# 计算 PageRank
pagerank = nx.pagerank(G)

# 打印结果
print("PageRank:", pagerank)
