import random
# Representação

def calcFitness(population):
    for element in population:
        fenotype = genotypeIntoFenotype(population)
    #Calculo do fitness, retorna [(genotipo, fitness),...]

def genotypeIntoFenotype(genotype):
    # 000000000000000000000000 -> [0,0,0,0,0,0.0,0]

    return fenotype



def Crossfill(child, parent,cutPoint):
    index = cutPoint
    while(len(child) < 8):
        if not(parent[index%8] in child):
            child += parent[index%8]
        index+=1
    return child

def cutAndCrossfill(parent1, parent2):
    fenoParent1 = genotypeIntoFenotype(parent1)
    fenoParent2 = genotypeIntoFenotype(parent2)
    cutPoint = random.randint(0,6)

    child1 = fenoParent1[0:cutPoint]
    child2 = fenoParent2[0:cutPoint]
    child1 = crossfill(child1,parent2,cutPoint)
    child2 = crossfill(child2,parent1,cutPoint)
    child1 = fenotypeIntoGenotype(child1)
    child2 = fenotypeIntoGenotype(child2)


    return [child1,child2]

def mutate(child):

    return mutatedChild

def parentSelection(parents):

    return selectedParents #2 parents

def survivalSelection(population):
    #Return survivors
    return newPopulation

def initPopulation(populationSize):
    #Creates a random population
    return population

def eval(populationFitness):

    return solution

def main():
    population = initPopulation(100)
    populationFitness = calcFitness(population)
    solution = eval(populationFitness)
    count = 0
    while(solution != None and count < 10000){
        
        count += 1
    }

    print(solution)