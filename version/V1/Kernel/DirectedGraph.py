import networkx as nx
import matplotlib.pyplot as plt
import random
import time  # 导入时间模块
import version.V1.Kernel.GraphBuffer as GB

# 创建连接矩阵
matrix = [[]]
# 初始化时间戳为0
timestamp = 0


def Generate_DirectedGraph():
    # 创建有向图
    Graph = nx.DiGraph()
    global matrix
    matrix = [[0 for _ in range(GB.MAX_NODE_SIZES + 1)] for _ in range(GB.MAX_NODE_SIZES + 1)]

    # 为结点创建一个整数范围
    nodes = range(1, GB.MAX_NODE_SIZES + 1)
    # 给图加边
    Graph.add_nodes_from(nodes)

    for pack in GB.edges_buffer:
        u = pack[0]
        v = pack[1]
        w = pack[2]
        # 如果边已存在，则不添加
        if not Graph.has_edge(u, v):
            Graph.add_edge(u, v)
            matrix[u][v] = w

    # 使用 spring layout，并自定义 k 参数
    pos = nx.spring_layout(Graph, k=10)  # 设置 k 参数

    # 生成节点的随机浅色，颜色强度转为颜色通道比例
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
    plt.savefig(f"./images/DirectedGraph/DAG_{timestamp}.png")
    plt.show()
