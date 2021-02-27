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

def fenotypeIntoGenotype(fenotype):
    def addZeros(element):
      missing = len(element)
      return (3-missing)*'0' + element
    
    return ''.join(map(addZeros, map(lambda x: "{0:b}".format(x), fenotype)))

def cutAndCrossfill(parent1, parent2):

   return child

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

main()