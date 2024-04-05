# matrix = [
#     [0, 0, 0.5, 1],
#     [0.5, 0, 0, 0],
#     [0.5, 1, 0, 0],
#     [0, 0, 0.5, 0]
# ]
# a = [0.25, 0.25, 0.25, 0.25]

matrix = [
    [0, 1, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]


# 这个类手动实现PageRank算法，与原生的比较
class PageRank:
    # 传进来的 max_iter 表示迭代次数，默认传进来100次，已经足够收敛
    # def __init__(self, max_iter, graph):
    def __init__(self, max_iter):
        self.max_iter = max_iter
        self.MarkovMatrix = None
        self.PR = None
        # self.graph = graph

    def construct_MarkovMatrix_PR(self):
        global matrix
        temp = matrix
        # 初始化马尔科夫矩阵
        self.MarkovMatrix = [[0.0 for _ in range(len(temp[0]))] for _ in range(len(temp))]
        # 通过temp矩阵来转化为马尔科夫矩阵
        for i in range(len(temp)):
            # cnt = sum(temp[i])
            cnt = 0
            for j in range(len(temp[0])):
                if temp[i][j] != 0:
                    cnt += 1
            # 先求出原来连接矩阵不为0的个数，然后下面再顺便转置求马尔科夫矩阵
            for k in range(len(temp)):
                if temp[i][k] != 0:
                    self.MarkovMatrix[k][i] = 1 / cnt
        # 构造PR矩阵
        length = len(temp)
        self.PR = [1.0 / length for _ in range(length)]

    # 由于下面三个方法没有使用类的实例属性或方法，所以添加装饰器@staticmethod设置为静态
    # 需要用到实例的时候把装饰器去掉即可
    # 原先的连接矩阵似乎不能很好的表示马尔科夫矩阵，所以很大概率是要把装饰器拿掉，加一个矩阵变量进来
    # @staticmethod

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

    # @staticmethod
    # 该函数解决某个结点只有一个出链且这个出链指向自己的情况
    def SpiderTraps(self):
        length = len(self.MarkovMatrix)
        beta = 0.85
        flag = False
        for i in range(length):
            if self.MarkovMatrix[i][i] == 1:
                flag = True
        if flag:
            for i in range(length):
                for j in range(length):
                    self.MarkovMatrix[i][j] = beta * self.MarkovMatrix[i][j] + (1 - beta) * (1 / length)

    # @staticmethod
    def page_rank(self):
        length = len(self.MarkovMatrix)
        # tmp用来存储新的PR矩阵
        tmp = [0] * length
        for _ in range(self.max_iter):
            for i in range(length):
                for j in range(length):
                    tmp[i] += self.MarkovMatrix[i][j] * self.PR[j]
            self.PR = tmp.copy()
            tmp = [0] * length

        rank_point_val = []
        for i in range(length):
            rank_point_val.append([0, chr(i + ord('a')), self.PR[i]])

        rank_point_val.sort(key=lambda x: x[2], reverse=True)

        for i in range(length):
            rank_point_val[i][0] = i + 1

        print(rank_point_val)

    def run_PageRank_algorithm(self):
        self.construct_MarkovMatrix_PR()
        self.DeadEnds()
        self.SpiderTraps()
        self.page_rank()


def main():
    # 创建 PageRank 类的实例
    pagerank = PageRank(max_iter=100)
    # 调用 run_all 方法，依次调用三个函数
    pagerank.run_PageRank_algorithm()


if __name__ == '__main__':
    main()
