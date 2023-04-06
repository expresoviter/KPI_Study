from random import randint, shuffle


class Graph:
    def __init__(self, nodesNumber, minPow, maxPow):
        self.V = nodesNumber  # Кількість вершин графа
        self.adjacencyList = [[] for i in range(self.V)]
        self.powers = [0 for i in range(self.V)]  # Степені вершин графа
        self.colourings = []  # Початкові розфарбування графа
        self.X = []
        self.Y = []
        # Генеруємо ребра так, щоб степінь відповідала умовам
        for i in range(self.V):
            degree = randint(minPow, maxPow)
            if self.powers[i] < degree:
                for j in range(self.powers[i], degree):
                    try:
                        connect = randint(i + 1, self.V - 1)
                    except ValueError:
                        continue
                    while self.powers[connect] == maxPow or connect == i or connect in self.adjacencyList[i]:
                        connect = randint(0, self.V - 1)
                    self.adjacencyList[i].append(connect)
                    self.adjacencyList[connect].append(i)
                    self.powers[i] += 1
                    self.powers[connect] += 1

    def firstColor(self, num):
        for i in range(num):
            current = [0 for i in range(self.V)]
            order = list(range(self.V))
            shuffle(order)
            for verge in order:
                neighbourColor = [current[neighbour] for neighbour in self.adjacencyList[verge]]
                curColor = 1
                while curColor in neighbourColor:
                    curColor += 1
                current[verge] = curColor
            self.colourings.append(current)

    def beesAlgorithm(self, bees):  # 5 розвідників, bees-5 фуражирів
        queue, vergeQueue, neighboursQueue = list(range(self.V)), [], []
        queue.sort(key=lambda x: self.powers[x])
        queue = queue[::-1]  # Черга з вершин з пріоритетом за спаданням степеня вершини
        for verge in queue:
            for neighbour in self.adjacencyList[verge]:
                vergeQueue.append(verge)
                neighboursQueue.append(neighbour)
        vergeQueues = [vergeQueue.copy() for i in range(len(self.colourings))]
        neighboursQueues = [neighboursQueue.copy() for i in range(len(self.colourings))]
        for i in range(1000):  # До 1000 ітерацій
            usedСolors = [max(i) for i in self.colourings]  # оцінка корисності ділянок
            if i == 0 or (i + 1) % 20 == 0:
                self.X.append(i)
                self.Y.append(min(usedСolors))
            chosenList = []
            while len(chosenList) != 4:
                randd = self.colourings[randint(0, len(self.colourings) - 1)]
                if randd not in chosenList:
                    chosenList.append(randd)
            mostPersp = self.colourings[usedСolors.index(min([max(l) for l in chosenList]))]
            random = self.colourings[randint(0, len(self.colourings) - 1)]
            while random == mostPersp:
                random = self.colourings[randint(0, len(self.colourings) - 1)]
            for forager in range(max(self.powers)):
                if not vergeQueues[self.colourings.index(mostPersp)]:
                    vergeQueues[self.colourings.index(mostPersp)] = vergeQueue.copy()
                    neighboursQueues[self.colourings.index(mostPersp)] = neighboursQueue.copy()
                self.search(mostPersp, vergeQueues[self.colourings.index(mostPersp)][0],
                            neighboursQueues[self.colourings.index(mostPersp)][0])
                vergeQueues[self.colourings.index(mostPersp)] = vergeQueues[
                                                                    self.colourings.index(mostPersp)][1:]
                neighboursQueues[self.colourings.index(mostPersp)] = neighboursQueues[self.colourings.index(
                    mostPersp)][1:]
            for forager in range(bees - 5 - max(self.powers)):
                if not vergeQueues[self.colourings.index(random)]:
                    vergeQueues[self.colourings.index(random)] = vergeQueue.copy()
                    neighboursQueues[self.colourings.index(random)] = neighboursQueue.copy()
                self.search(random, vergeQueues[self.colourings.index(random)][0],
                            neighboursQueues[self.colourings.index(random)][0])
                vergeQueues[self.colourings.index(random)] = vergeQueues[self.colourings.index(random)][1:]
                neighboursQueues[self.colourings.index(random)] = neighboursQueues[self.colourings.index(random)][1:]
        return self.colourings[usedСolors.index(min(usedСolors))]

    def search(self, colouring, verge, neighbour):  # пошук перестановок кольорів
        colouring[verge], colouring[neighbour] = colouring[neighbour], colouring[verge]
        noConflicts = 1
        for conflict in self.adjacencyList[verge]:
            if colouring[verge] == colouring[conflict]:
                noConflicts = 0
                break
        for conflict in self.adjacencyList[neighbour]:
            if colouring[neighbour] == colouring[conflict]:
                noConflicts = 0
                break
        if noConflicts:
            if colouring[verge] > colouring[neighbour]:
                self.reduce(colouring, verge)
                self.reduce(colouring, neighbour)
            else:
                self.reduce(colouring, neighbour)
                self.reduce(colouring, verge)
        else:
            colouring[verge], colouring[neighbour] = colouring[neighbour], colouring[verge]

    def reduce(self, colouring, verge):
        curColor = colouring[verge]
        for changeColor in range(1, colouring[verge]):
            colouring[verge] = changeColor
            noConflict = 1
            for neighbour in self.adjacencyList[verge]:
                if colouring[verge] == colouring[neighbour]:
                    noConflict = 0
                    colouring[verge] = curColor
                    break
            if noConflict:
                break
