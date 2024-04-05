import random
import version.V1.Kernel.GraphBuffer as GB


# 随机选取出点和入点，并随机生成权重
def random_edges():
    u = random.randint(1, GB.MAX_NODE_SIZES)
    v = random.randint(1, GB.MAX_NODE_SIZES)
    weight = random.randint(1, GB.MAX_WEIGHT)
    # 返回一个三元组
    return u, v, weight
