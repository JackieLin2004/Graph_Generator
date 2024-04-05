# 封装成类
class GraphBuffer:
    def __init__(self):
        # 存放u、v、w三元组
        self.edges_buffer = []
        self.MAX_NODE_SIZES = 0
        self.MAX_EDGE_SIZES = 0
        self.MAX_WEIGHT = 9
        self.MIN_WEIGHT = 1
        # 有向图还是无向图
        self.Gtype = 0
        # 连接矩阵
        self.matrix = [[]]
