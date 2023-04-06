from random import randint, random
import sys

global nodesNumber
nodesNumber = 300
global populNumber
populNumber = 8
global mutationNum
global lINum
mutationNum = 2
lINum = 2


class Node:
    def __init__(self, value=0):
        self.value = value
        self.degree = 0
        self.edges = []

    def addEdge(self, v):
        self.edges.append(v)


class SortedListNode:
    def __init__(self):
        self.node = -1
        self.reach = 0


class Graph:
    def __init__(self):
        self.aMatrix = [[0 for j in range(nodesNumber)] for i in range(nodesNumber)]
        self.nodes = [None for i in range(nodesNumber)]
        self.powers = [0 for i in range(nodesNumber)]
        self.sortedNodes = []

    def addEdge(self, sv, ev):
        self.aMatrix[sv][ev] = 1
        self.aMatrix[ev][sv] = 1
        node = self.nodes[sv]
        if node is None:
            node = Node(sv)
            self.nodes[sv] = node
            node.addEdge(ev)
            self.sortedNodes.append(node)
            node.degree += 1
        else:
            node.addEdge(ev)
            node.degree += 1
        node = self.nodes[ev]
        if node is None:
            node = Node(ev)
            self.nodes[ev] = node
            node.addEdge(sv)
            self.sortedNodes.append(node)
            node.degree += 1
        else:
            node.addEdge(sv)
            node.degree += 1

    def sortList(self):
        self.sortedNodes.sort(key=lambda x: x.degree, reverse=True)


global graph
graph = Graph()


class Clique:
    def __init__(self, firstVertex="def"):
        self.clique = []
        self.pa = []
        self.mapPA = dict()
        self.mapClique = dict()
        if firstVertex != "def":
            self.clique.append(firstVertex)
            self.mapClique[firstVertex] = True
            for i in range(nodesNumber):
                if i == firstVertex:
                    continue
                elif graph.aMatrix[i][firstVertex] == 1:
                    self.pa.append(i)
                    self.mapPA[i] = True

    def addVertex(self, vertex):
        if self.containsInClique(vertex):
            return
        self.clique.append(vertex)
        self.mapClique[vertex] = True
        self.eraseFromPA(vertex)
        erasedNodes = []
        for i in range(len(self.pa)):
            pavertex = self.pa[i]
            if graph.aMatrix[pavertex][vertex] == 0:
                erasedNodes.append(pavertex)
        for i in range(len(erasedNodes)):
            self.eraseFromPA(erasedNodes[i])

    def removeVertex(self, vertex):
        if not (self.containsInClique(vertex)):
            return
        self.eraseFromClique(vertex)
        for i in range(nodesNumber):
            if self.containsInClique(i):
                continue
            else:
                flag = True
                for n in range(len(self.clique)):
                    ver = self.clique[n]
                    if graph.aMatrix[i][ver] == 0:
                        flag = False
                        break
                if flag:
                    if not i in self.mapPA:
                        self.pa.append(i)
                        self.mapPA[i] = True

    def eraseFromPA(self, vertex):
        self.mapPA.pop(vertex)
        if vertex in self.pa:
            self.pa.remove(vertex)

    def containsInPA(self, vertex):
        return (vertex in self.mapPA)

    def eraseFromClique(self, vertex):
        self.mapClique.pop(vertex)
        if vertex in self.clique:
            self.clique.remove(vertex)

    def containsInClique(self, vertex):
        for i in self.mapClique:
            if self.mapClique[i] == vertex:
                return True
        return False

    def computeSortedList(self):
        sortedList = []
        for i in range(len(self.pa)):
            node1 = self.pa[i]
            reach = 0
            for j in range(len(self.pa)):
                if i == j:
                    continue
                node2 = self.pa[j]
                if graph.aMatrix[node1][node2] == 1:
                    reach += 1
            n = SortedListNode()
            n.reach = reach
            n.node = node1
            sortedList.append(n)
        sortedList.sort(key=lambda x: x.reach, reverse=True)
        return sortedList

    def clone(self):
        cpa = []
        cclique = []
        for i in range(len(self.pa)):
            cpa.append(self.pa[i])
        for i in range(len(self.clique)):
            cclique.append(self.clique[i])
        cMapPa = dict(self.mapPA)
        cMapClique = dict(self.mapClique)
        clone = Clique()
        clone.clique = cclique
        clone.pa = cpa
        clone.mapPA = cMapPa
        clone.mapClique = cMapClique
        return clone


def generateRandomPopulation():
    population = []
    flags = [False for i in range(nodesNumber)]
    for i in range(populNumber):
        rand = randint(0, nodesNumber - 1)
        cntt = 0
        while flags[rand]:
            cntt += 1
            if cntt > nodesNumber:
                break
            rand = randint(0, nodesNumber - 1)
        flags[rand] = True
        clique = Clique(rand)
        sortedList = clique.computeSortedList()
        cnt = 0
        while len(clique.pa) > 0:
            if cnt == len(sortedList):
                break
            node = sortedList[cnt].node
            cnt += 1
            if clique.containsInPA(node):
                clique.addVertex(node)
        population.append(clique)
    node = graph.sortedNodes[0].value
    clique = Clique(node)
    sortedList = clique.computeSortedList()
    count = 0
    while len(clique.pa) > 0:
        node = sortedList[count].node
        count += 1
        if clique.containsInPA(node):
            clique.addVertex(node)
    population.append(clique)
    return population


def greedyCrossover(c1, c2):
    vec = []
    flags = [False for i in range(nodesNumber)]
    for i in range(len(c1.clique)):
        vertex = c1.clique[i]
        if not (flags[vertex]):
            vec.append(vertex)
            flags[vertex] = True

    for i in range(len(c2.clique)):
        vertex = c2.clique[i]
        if not (flags[vertex]):
            vec.append(vertex)
            flags[vertex] = True

    sortedList = []
    for i in range(len(vec)):
        node1 = vec[i]
        reach = 0
        for j in range(len(vec)):
            if i == j:
                continue
            node2 = vec[j]
            if graph.aMatrix[node1][node2] == 1:
                reach += 1
        sNode = SortedListNode()
        sNode.reach = reach
        sNode.node = node1
        sortedList.append(sNode)
    sortedList.sort(key=lambda x: x.reach, reverse=True)
    firstVertex = sortedList[0].node
    clique = Clique(firstVertex)
    count = 1
    while count < len(sortedList):
        node = sortedList[count].node
        if clique.containsInPA(node):
            clique.addVertex(node)
        count += 1
    while len(clique.pa) > 0:
        node = clique.pa[0]
        clique.addVertex(node)
    return clique


def intersectionCrossover(c1, c2):
    intersect = []
    flags = [False for i in range(nodesNumber)]
    for i in range(len(c2.clique)):
        vertex = c2.clique[i]
        flags[vertex] = True
    for i in range(len(c1.clique)):
        ver1 = c1.clique[i]
        if flags[ver1]:
            intersect.append(ver1)
    if len(intersect) == 0:
        return greedyCrossover(c1, c2)
    vertex = intersect[0]
    clique = Clique(vertex)
    for i in range(1, len(intersect)):
        vertex = intersect[i]
        if clique.containsInPA(vertex):
            clique.addVertex(vertex)
    if len(clique.pa) > 0:
        sortedList = clique.computeSortedList()
        cnt = 0
        while len(clique.pa) > 0:
            if cnt==len(sortedList):
                break
            node = sortedList[cnt].node
            cnt += 1
            if clique.containsInPA(node):
                clique.addVertex(node)
    return clique


def randomSelection(population):
    parents = []
    rand1 = randint(0, populNumber)
    rand2 = randint(0, populNumber)
    while rand1 == rand2:
        rand1 = randint(0, populNumber)
        rand2 = randint(0, populNumber)
    p1 = population[rand1]
    p2 = population[rand2]
    parents.append(p1)
    parents.append(p2)
    return parents


def localImprovement(clique):
    gBest = clique.clone()
    for i in range(lINum):  # LOCAL IMPROVEMENT
        rand1 = randint(0, len(clique.clique) - 1)
        rand2 = randint(0, len(clique.clique) - 1)
        countt = 0
        while rand1 == rand2:
            countt += 1
            if countt > 100:
                break
            rand1 = randint(0, len(clique.clique) - 1)
            rand2 = randint(0, len(clique.clique) - 1)
        vertex1 = clique.clique[rand1]
        vertex2 = clique.clique[rand2]
        clique.removeVertex(vertex1)
        clique.removeVertex(vertex2)
        sortedList = clique.computeSortedList()
        count = 0
        while len(clique.pa) > 0:
            node = sortedList[count].node
            count += 1
            if node >= nodesNumber:
                sys.exit("Node greater", node)
            if clique.containsInPA(node):
                clique.addVertex(node)
        if len(gBest.clique) < len(clique.clique):
            gBest = clique.clone()
    clique = gBest
    return clique


def mutate(clique):
    flags = [False for i in range(nodesNumber)]
    for i in range(mutationNum):  # MUTATIONS
        rand = randint(0, len(clique.clique) - 1)
        count = 0
        while flags[rand]:
            rand = randint(0, len(clique.clique) - 1)
            count += 1
            if count > 100:
                break
        flags[rand] = True
        vertex = clique.clique[rand]
        clique.removeVertex(vertex)
    rand = random()
    if rand < 0.5:
        sortedList = clique.computeSortedList()
        cnt = 0
        while len(clique.pa) > 0:
            if cnt==len(sortedList):
                break
            node = sortedList[cnt].node
            cnt += 1
            if clique.containsInPA(node):
                clique.addVertex(node)
    else:
        while len(clique.pa) > 0:
            rand = randint(0, len(clique.pa) - 1)
            vertex = clique.pa[rand]
            clique.addVertex(vertex)
