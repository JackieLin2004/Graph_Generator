import networkx as nx
import matplotlib.pyplot as plt
import random
import time  # 导入时间模块


class DAGgenerator:
    def __init__(self):
        self.timestamp = 0

    def Generate_DirectedGraph(self, graph):
        # 创建有向图
        DGraph = nx.DiGraph()
        graph.matrix = [[0 for _ in range(graph.MAX_NODE_SIZES + 1)] for _ in range(graph.MAX_NODE_SIZES + 1)]

        nodes = range(1, graph.MAX_NODE_SIZES + 1)
        DGraph.add_nodes_from(nodes)

        for pack in graph.edges_buffer:
            u = pack[0]
            v = pack[1]
            w = pack[2]
            # 如果边已存在，则不添加
            if not DGraph.has_edge(u, v):
                DGraph.add_edge(u, v)
                graph.matrix[u][v] = w

        # 使用 spring layout，并自定义 k 参数
        pos = nx.spring_layout(DGraph, k=10)  # 设置 k 参数

        # 生成节点的随机浅色，颜色强度转为颜色通道比例
        node_colors = [(random.randint(100, 255) / 255, random.randint(100, 255) / 255, random.randint(100, 255) / 255)
                       for
                       _ in
                       nodes]

        # 绘制无向图
        nx.draw(DGraph, pos, with_labels=True, node_color=node_colors, node_size=300, edge_color='grey', linewidths=1,
                font_size=9)

        # 获取当前时间戳
        self.timestamp = int(time.time())
        # 保存图片到计算机，并使用时间戳命名
        plt.savefig(f"./images/DirectedGraph/DAG_{self.timestamp}.png")
        plt.show()

    # 绘制最短路的图
    @staticmethod
    def GenerateDAGShortestPathGraphic(graph, sp):
        # 创建有向图
        DGraph = nx.DiGraph()
        nodes = range(1, graph.MAX_NODE_SIZES + 1)
        DGraph.add_nodes_from(nodes)

        for i in range(1, graph.MAX_NODE_SIZES + 1):
            for j in range(1, graph.MAX_NODE_SIZES + 1):
                if graph.matrix[i][j] != 0:
                    DGraph.add_edge(i, j)

        # 绘图
        pos = nx.random_layout(DGraph)
        nx.draw(DGraph, pos, with_labels=True, node_color='skyblue', node_size=300, edge_color='grey',
                linewidths=1,
                font_size=9)

        # 标记最短路径上的边
        for i in range(len(sp) - 1):
            node1 = sp[i]
            node2 = sp[i + 1]
            nx.draw_networkx_edges(DGraph, pos, edgelist=[(node1, node2)], edge_color='red', width=2)

        # 标记最短路径上的点
        nx.draw_networkx_nodes(DGraph, pos, nodelist=sp, node_color='red', node_size=300)
        plt.savefig(f"./temp/DAG_SP.png")
        plt.show()
