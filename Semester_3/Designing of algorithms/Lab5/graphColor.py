import networkx as nx
import matplotlib.pyplot as plt


class graphVisualisation:
    def __init__(self):
        self.visual = []

    def addEdges(self, aMatrix,s):
        for i in range(s):
            for j in range(s):
                if aMatrix[i][j]==1:
                    self.visual.append([i, j])

    def visualize(self, color,k):
        g = nx.Graph()
        g.add_nodes_from([i for i in range(k)])
        g.add_edges_from(self.visual)
        nx.draw_networkx(g, node_color=color,with_labels=True)
        plt.show()

