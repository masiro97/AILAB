import random
def knapsack(V,W,MAX,popSize,mut,maxGen,percent):
    generation = 0
    pop = generate(V,popSize)
    fitness = getFitness(pop,V,W,MAX)
    while(not test(fitness,percent) and generation < maxGen):
        generation += 1
        pop = newPopulation(pop,fitness,mut)
        fitness = getFitness(pop,V,W,MAX)
        #print fitness
        #print generation
        return selectElite(pop,fitness)


def generate(V,popSize):
    length = len(V)
    pop = [[random.randint(0,1)for i in range(length)]]

def test();
def newPopulation():
def getFitness(pop,V,W,MAX):
    fitness = []

    for i in range(len(pop)):
        weight = 0
        volume = MAX + 1
        while(volume > MAX):
            weight = 0
            volume = 0
            ones = []

            for j in range(len([pop[i]])):
                if pop[i][j] == 1:
                    volume += V[j]
                    weight += W[j]
                    ones += [j]
                if volume > MAX:
                    pop[i][ones[random.randint(0,len(ones)-1)]] = 0

def selectElite():
