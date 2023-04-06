from clique import *
from graphColor import *
from datetime import datetime


def main():
    for i in range(nodesNumber):
        degree = randint(2,30)
        if graph.powers[i] < degree:
            for j in range(graph.powers[i], degree):
                try:
                    connect = randint(i + 1, nodesNumber - 1)
                except ValueError:
                    continue
                while graph.powers[connect] == 30 or connect == i:
                    connect = randint(0, nodesNumber - 1)
                graph.addEdge(i, connect)
                graph.powers[i] += 1
                graph.powers[connect] += 1

    s = datetime.now()
    graph.sortList()
    population = generateRandomPopulation()
    population.sort(key=lambda x: len(x.clique), reverse=True)
    gBest = population[0].clone()
    prevBest = len(gBest.clique)
    cnt = 0
    for n in range(1000):
        if prevBest == len(gBest.clique):
            cnt += 1
            if cnt > 10:
                pop = generateRandomPopulation()
                pop, population = population, pop
                cnt = 0
        else:
            prevBest = len(gBest.clique)
            cnt = 0
        newPopulation = []
        population.sort(key=lambda x: len(x.clique), reverse=True)
        localBest = population[0]
        if len(gBest.clique) < len(localBest.clique):
            gBest = localBest.clone()
        gBest = localImprovement(gBest)
        newPopulation.append(gBest)
        print("Iteration", n, "-", "size of the biggest clique =", len(gBest.clique))
        for i in range(populNumber):
            parents = randomSelection(population)
            offspring = intersectionCrossover(parents[0], parents[1])
            offspring = localImprovement(offspring)
            if len(offspring.clique) <= len(parents[0].clique) or len(offspring.clique) <= len(parents[1].clique):
                mutate(offspring)
            newPopulation.append(offspring)
        population, newPopulation = newPopulation, population
    print("Vertices in the Clique:", len(gBest.clique))
    print([i + 1 for i in gBest.clique])
    s = datetime.now() - s
    print(s)

    g = graphVisualisation()
    g.addEdges(graph.aMatrix, nodesNumber)
    color = ["blue" for _ in range(nodesNumber)]
    for i in gBest.clique:
        color[i] = "red"
    g.visualize(color, nodesNumber)


if __name__ == "__main__":
    main()
    del graph
