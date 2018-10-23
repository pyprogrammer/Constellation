import networkx as nx


class ProgramGraph:
    """
    A Program Graph is a directed bipartite acyclic graph. We have compute nodes (C), and data format
    nodes (D). Compute nodes
    """
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node):
        self.graph.add_node(node)

