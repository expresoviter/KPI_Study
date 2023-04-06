from algorithm import *
import matplotlib.pyplot as matplot
from graphColor import *

if __name__ == '__main__':
    graph = Graph(300, 1, 50)
    graph.firstColor(int(input("Введіть кількість початкових розфарбувань: ")))
    last = graph.beesAlgorithm(60)

    g = graphVisualisation()
    last = g.numToCol(last)
    g.addEdges(graph.adjacencyList)
    g.visualize(last, 300)

    matplot.plot(graph.X,graph.Y)
    matplot.xlabel('Кількість ітерацій')
    matplot.ylabel('Кількість кольорів в найкращому розфарбуванні')
    matplot.show()
