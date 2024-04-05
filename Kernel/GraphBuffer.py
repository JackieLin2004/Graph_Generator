class GraphBuffer:
    def __init__(self):
        self.edges_buffer = []
        self.MAX_NODE_SIZES = 0
        self.MAX_EDGE_SIZES = 0
        self.MAX_WEIGHT = 9
        self.MIN_WEIGHT = 1
        self.Gtype = 0
        self.matrix = [[]]
