# Representação
import random

def calcFitness(population):
    result = []
    fenotype_list = list(map(genotypeIntoFenotype, population))
    for fenotype in fenotype_list:
        penalty = 1
        for idx, element in enumerate(fenotype):
            for idx2, el in enumerate(fenotype):
                penalty += 1 if (idx != idx2 and abs(idx - idx2) == abs(element - el)) else 0
        result.append((fenotype, 1/penalty))
    return result

def genotypeIntoFenotype(genotype):
    # 000000000000000000000000 -> [0,0,0,0,0,0.0,0]
    actual = 0
    fenotype = []
    for i in range(3, len(genotype)+3, 3):
        fenotype.append(int(genotype[(actual*3):i],2))
        actual += 1

    return fenotype


def fenotypeIntoGenotype(fenotype):
    def addZeros(element):
        missing = len(element)
        return (3-missing)*'0' + element
    
    return ''.join(map(addZeros, map(lambda x: "{0:b}".format(x), fenotype)))

def crossfill(child, parent,cutPoint):
    index = cutPoint
    while(len(child) < 8):
        if not(parent[index] in child):
            child.append(parent[index])
        index= (index + 1)%8
    return child

def cutAndCrossfill(parent1, parent2):
    fenoParent1 = genotypeIntoFenotype(parent1)
    fenoParent2 = genotypeIntoFenotype(parent2)
    print(fenoParent1)
    print(fenoParent2)
    cutPoint = random.randint(0,6)

    child1 = fenoParent1[0:cutPoint]
    child2 = fenoParent2[0:cutPoint]
    child1 = crossfill(child1,fenoParent2,cutPoint)
    child2 = crossfill(child2,fenoParent1,cutPoint)
    print(child1)
    print(child2)
    child1 = fenotypeIntoGenotype(child1)
    child2 = fenotypeIntoGenotype(child2)

    return [child1,child2]

def mutate(child):
   position1 = random.randint(0,7)
   position2 = random.randint(0,7)
   while position1 == position2:
        position1 = random.randint(0,7)
        position2 = random.randint(0,7)
   child[position1], child[position2] = child[position2], child[position1]
   return child

def parent_selection(population):
    parents = select_random_parents(population)
    parents.sort(key=lambda tup: tup[1], reverse=True)
    selectedParents = parents[0:2]
    return selectedParents #2 parents

def select_random_parents(population):
    randomParents = []
    for i in range(5):
        randomParents.append(population[random.randint(0,100)])
    return randomParents
    
def survivalSelection(population):
    population.sort(key=lambda tup: -tup[1])
    return population[:-2]

def initPopulation(populationSize):
    #Creates a random population
    population = []
    while populationSize > 0:
        population.append(generateChild())
        populationSize -= 1
    return population

def generateChild():
    child = ""
    count = 0
    while count < 24:
        randomNumber = random.random()
        if randomNumber <= 0.5:
            child = child + "0"
        else:
            child = child + "1"
        count += 1
    return child

def eval(populationFitness):
    for individual in populationFitness:
        if individual[1] == 1:
            return individual[0]
    
    return None

def main():
    # parent1 = [0,2,4,1,5,3,6,7]
    # parent2 = [7,6,5,4,3,2,1,0]
    # parent1 = fenotypeIntoGenotype(parent1)
    # parent2 = fenotypeIntoGenotype(parent2)
    # cutAndCrossfill(parent1,parent2)
    population = initPopulation(100)
    print(population)
    populationFitness = calcFitness(population)
    solution = eval(populationFitness)
    count = 0
    while solution != None and count < 10000:
      count += 1
    

    print(solution)

main()
