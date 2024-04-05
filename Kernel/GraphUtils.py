import random


# 随机选取出点和入点，并随机生成权重
def random_edges(graph):
    u = 0
    v = 0
    weight = 0
    while weight == 0:
        u = random.randint(1, graph.MAX_NODE_SIZES)
        v = random.randint(1, graph.MAX_NODE_SIZES)
        weight = random.randint(graph.MIN_WEIGHT, graph.MAX_WEIGHT)
    return u, v, weight
