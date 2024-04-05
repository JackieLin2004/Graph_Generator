import networkx as nx


# 手动模拟PageRank算法
class PageRank:
    def __init__(self):
        # max_iter 表示迭代次数，默认传进来100次，已经足够收敛
        self.max_iter = 100
        self.MarkovMatrix = None
        self.PR = None

    # 导入连接矩阵，运算出马尔科夫矩阵以及PR矩阵
    def construct_MarkovMatrix_PR(self, matrix):
        temp = [[0 for _ in range(len(matrix) - 1)] for _ in range(len(matrix) - 1)]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix)):
                if matrix[i][j] != 0:
                    temp[i - 1][j - 1] = 1

        self.MarkovMatrix = [[0.0 for _ in range(len(temp))] for _ in range(len(temp))]
        for i in range(len(temp)):
            cnt = sum(temp[i])
            for k in range(len(temp)):
                if temp[i][k] != 0:
                    self.MarkovMatrix[k][i] = 1 / cnt
        self.PR = [1.0 / len(temp) for _ in range(len(temp))]

    # 该函数解决某个结点只有入链没有出链的情况
    def DeadEnds(self):
        length = len(self.MarkovMatrix)
        for i in range(length):
            flag = True
            # 检查一列是否全部为0
            for j in range(length):
                if self.MarkovMatrix[j][i] != 0:
                    flag = False
            if flag:
                for k in range(length):
                    self.MarkovMatrix[k][i] += 1 / length

    # 该函数解决某个结点只有一个出链且这个出链指向自己的情况
    def SpiderTraps(self):
        beta = 0.85
        length = len(self.MarkovMatrix)
        for i in range(length):
            for j in range(length):
                self.MarkovMatrix[i][j] = beta * self.MarkovMatrix[i][j] + (1 - beta) * (1 / length)

    # 执行PageRank算法
    def page_rank(self):
        length = len(self.MarkovMatrix)

        tmp = [0] * length

        for _ in range(self.max_iter):
            for i in range(length):
                for j in range(length):
                    tmp[i] += self.MarkovMatrix[i][j] * self.PR[j]
            self.PR = tmp.copy()
            tmp = [0] * length
        rank_point_val = []
        for i in range(length):
            rank_point_val.append([0, i + 1, self.PR[i]])

        rank_point_val.sort(key=lambda x: x[2], reverse=True)

        for i in range(length):
            rank_point_val[i][2] = round(rank_point_val[i][2], 14)

        for i in range(length):
            rank_point_val[i][0] = i + 1
        return rank_point_val

    # 运行PageRank算法全过程
    def run_Implemented_PageRank_algorithm(self, matrix):
        self.construct_MarkovMatrix_PR(matrix)
        self.DeadEnds()
        self.SpiderTraps()
        rpv = self.page_rank()
        return rpv

    # 原生库实现的PageRank算法，用以做比较
    @staticmethod
    def run_Lib_PageRank_algorithm(matrix):
        G = nx.DiGraph()
        G.add_nodes_from(range(1, len(matrix)))
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] != 0:
                    G.add_edge(i, j)
        pg = nx.pagerank(G)
        return pg
