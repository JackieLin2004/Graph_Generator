matrix = [
    [0, 0, 0.5, 1],
    [0.5, 0, 0, 0],
    [0.5, 1, 0, 0],
    [0, 0, 0.5, 0]
]
a = [0.25, 0.25, 0.25, 0.25]


# 这个类手动实现PageRank算法，与原生的比较
class PageRank:
    # 传进来的 max_iter 表示迭代次数，默认传进来100次，已经足够收敛
    def __init__(self, max_iter):
        self.max_iter = max_iter

    # 由于下面三个方法没有使用类的实例属性或方法，所以添加装饰器@staticmethod设置为静态
    # 需要用到实例的时候把装饰器去掉即可
    # 原先的连接矩阵似乎不能很好的表示马尔科夫矩阵，所以很大概率是要把装饰器拿掉，加一个矩阵变量进来
    @staticmethod
    def DeadEnds():
        global matrix
        length = len(matrix)
        for i in range(length):
            flag = True
            for j in range(length):
                if matrix[j][i] != 0:
                    flag = False
            if flag:
                for k in range(length):
                    matrix[k][i] = 1 / length

    @staticmethod
    def SpiderTraps():
        global matrix
        length = len(matrix)
        beta = 0.85
        flag = False
        for i in range(length):
            if matrix[i][i] != 0:
                flag = True
        if flag:
            for i in range(length):
                for j in range(length):
                    matrix[i][j] = beta * matrix[i][j] + (1 - beta) * (1 / length)

    @staticmethod
    def page_rank(n):
        global matrix
        length = len(matrix)
        global a
        tmp = [0] * length
        for _ in range(n):
            for i in range(length):
                for j in range(length):
                    tmp[i] += matrix[i][j] * a[j]
            a = tmp
            tmp = [0] * length

        rank_point_val = []
        for i in range(length):
            rank_point_val.append([0, chr(i + ord('a')), a[i]])

        rank_point_val.sort(key=lambda x: x[2], reverse=True)

        for i in range(length):
            rank_point_val[i][0] = i + 1

        print(rank_point_val)

    def run(self):
        self.DeadEnds()
        self.SpiderTraps()
        self.page_rank(self.max_iter)


def main():
    # 创建 PageRank 类的实例
    pagerank = PageRank(max_iter=100)
    # 调用 run_all 方法，依次调用三个函数
    pagerank.run()


if __name__ == '__main__':
    main()
