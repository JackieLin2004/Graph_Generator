import networkx as nx
import matplotlib.pyplot as plt
import random
import time  # 导入时间模块
import version.V1.Kernel.GraphBuffer as GB

# 创建连接矩阵
matrix = [[]]
# 初始化时间戳为0
timestamp = 0


def Generate_UndirectedGraph():
    # 创建无向图
    Graph = nx.Graph()
    global matrix
    # 初始化把连接矩阵的值全部设为0
    matrix = [[0 for _ in range(GB.MAX_NODE_SIZES + 1)] for _ in range(GB.MAX_NODE_SIZES + 1)]

    # 为结点创建一个整数范围
    nodes = range(1, GB.MAX_NODE_SIZES + 1)
    # 给图加边
    Graph.add_nodes_from(nodes)

    # buffer里面存的是pack，而pack里面存的是一个三元组
    for pack in GB.edges_buffer:
        u = pack[0]
        v = pack[1]
        w = pack[2]
        # 如果边已存在，则不添加
        if not Graph.has_edge(u, v):
            Graph.add_edge(u, v)
            Graph.add_edge(v, u)
            matrix[u][v] = w
            matrix[v][u] = w

    # 使用 spring layout来计算结点的布局，并将结果存在pos中
    # 自定义 k 参数，参数k类似于弹簧的劲度系数，表现的是每个点之间的相对吸引力，越大距离越远
    pos = nx.spring_layout(Graph, k=10)

    # 生成节点的随机浅色
    node_colors = [(random.randint(100, 255) / 255, random.randint(100, 255) / 255, random.randint(100, 255) / 255) for
                   _ in
                   nodes]

    # 绘制无向图
    nx.draw(Graph, pos, with_labels=True, node_color=node_colors, node_size=300, edge_color='grey', linewidths=1,
            font_size=9)

    # 获取当前时间戳
    global timestamp
    timestamp = int(time.time())
    # 保存图片到计算机，并使用时间戳命名
    plt.savefig(f"./images/UndirectedGraph/UDG_{timestamp}.png")
    plt.show()
