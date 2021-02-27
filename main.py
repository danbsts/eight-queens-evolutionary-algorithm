# Representação
import random

def calcFitness(population):
   for element in population:
       fenotype = genotypeIntoFenotype(population)
    #Calculo do fitness, retorna [(genotipo, fitness),...]

def genotypeIntoFenotype(genotype):
    # 000000000000000000000000 -> [0,0,0,0,0,0.0,0]
    actual = 0
    fenotype = []
    for i in range(3, len(genotype)+3, 3):
        fenotype.append(int(genotype[(actual*3):i],2))
        actual += 1

    return fenotype

def Crossfill(child, parent,cutPoint):
    index = cutPoint
    while(len(child) < 8):
        if not(parent[index%8] in child):
            child += parent[index%8]
        index+=1
    return child

def fenotypeIntoGenotype(fenotype):
    def addZeros(element):
      missing = len(element)
      return (3-missing)*'0' + element
    
    return ''.join(map(addZeros, map(lambda x: "{0:b}".format(x), fenotype)))

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
   position1 = random.randint(0,7)
   position2 = random.randint(0,7)
   while position1 == position2:
        position1 = random.randint(0,7)
        position2 = random.randint(0,7)
   child[position1], child[position2] = child[position2], child[position1]
   return child

def parentSelection(parents):
   return selectedParents #2 parents

def survivalSelection(population):
    #Return survivors
   return newPopulation

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

   return solution

def main():
    population = initPopulation(10)
    print(population)
    populationFitness = calcFitness(population)
    solution = eval(populationFitness)
    count = 0
    while(solution != None and count < 10000){
        
        count += 1
    }

    print(solution)

main()