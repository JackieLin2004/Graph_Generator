import random
import Kernel.GraphBuffer as GB


def random_edges():
    u = random.randint(1, GB.MAX_NODE_SIZES)
    v = random.randint(1, GB.MAX_NODE_SIZES)
    weight = random.randint(1, GB.MAX_WEIGHT)
    return u, v, weight
