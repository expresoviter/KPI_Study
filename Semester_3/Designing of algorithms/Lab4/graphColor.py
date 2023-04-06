import networkx as nx
import matplotlib.pyplot as plt


class graphVisualisation:
    def __init__(self):
        self.visual = []

    def addEdges(self, adjacency):
        for i in range(len(adjacency)):
            for j in adjacency[i]:
                self.visual.append([i, j])

    def numToCol(self, list):
        dict = {1: "red", 2: "orange", 3: "yellow", 4: "green", 5: "cyan", 6: "blue", 7: "violet", 8: "gold",
                9: "limegreen", 10: "darkorange", 11: "pink", 12: "magenta", 13: "grey", 14: "black"}
        for i in dict:
            list = repl(list, i, dict[i])
        return list

    def visualize(self, color,k):
        g = nx.Graph()
        g.add_nodes_from([i for i in range(k)])
        g.add_edges_from(self.visual)
        nx.draw_networkx(g, node_color=color,with_labels=True)
        plt.show()


def repl(list, item, to):
    return [to if it == item else it for it in list]
