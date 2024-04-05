import networkx as nx


class PageRank:
    def __init__(self):
        self.max_iter = 100
        self.MarkovMatrix = None
        self.PR = None

    def construct_MarkovMatrix_PR(self, matrix):
        temp = [[0 for i in range(len(matrix) - 1)] for j in range(len(matrix) - 1)]
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

    def SpiderTraps(self):
        beta = 0.85
        length = len(self.MarkovMatrix)
        for i in range(length):
            for j in range(length):
                self.MarkovMatrix[i][j] = beta * self.MarkovMatrix[i][j] + (1 - beta) * (1 / length)

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

    def run_Implemented_PageRank_algorithm(self, matrix):
        self.construct_MarkovMatrix_PR(matrix)
        self.DeadEnds()
        self.SpiderTraps()
        rpv = self.page_rank()
        return rpv

    def run_Lib_PageRank_algorithm(self, matrix):
        G = nx.DiGraph()
        G.add_nodes_from(range(1, len(matrix)))
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] != 0:
                    G.add_edge(i, j)
        pg = nx.pagerank(G)
        return pg
