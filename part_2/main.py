import random
import numpy as np
from functools import reduce

from functools import reduce
def calculate_fitness(population):
    result = []
    for fenotype in population:
        penalty = 1
        for idx, element in enumerate(fenotype):
            for idx2, el in enumerate(fenotype):
                penalty += 1 if (idx != idx2 and abs(idx - idx2) == abs(element - el)) else 0
        result.append((fenotype, 1/penalty))
    return result

def crossfill(child, parent,cut_point):
    index = cut_point
    while(len(child) < 8):
        if not(parent[index] in child):
            child.append(parent[index])
        index= (index + 1)%8
    return child

def cut_and_crossfill(parents):
    if random.random() <= 0.9:
        parent1 = parents[0]
        parent2 = parents[1]
        cut_point = random.randint(0,6)

        child1 = parent1[0:cut_point]
        child2 = parent2[0:cut_point]
        child1 = crossfill(child1,parent2,cut_point)
        child2 = crossfill(child2,parent1,cut_point)
    else:
        child1 = parents[0]
        child2 = parents[1]

    return [child1,child2]

def mutate(child):
   position1 = random.randint(0,7)
   position2 = random.randint(0,7)
   while position1 == position2:
        position1 = random.randint(0,7)
        position2 = random.randint(0,7)
   child[position1], child[position2] = child[position2], child[position1]
   return child

def spin_wheel(roleta, sorted_probability):
    for idx, probability in enumerate(roleta):
        if idx > 0:
            if(sorted_probability <= probability and sorted_probability > roleta[idx-1]):
                break
        else:
            if(sorted_probability <= probability):
                break
    return idx
def parent_selection(population):
    #parents = select_random_parents(population)
    total_fitness = reduce(lambda x,y: x + y[1], population,0)
    parents = population
    roleta = []
    current_probability=0
    selected_parents = []
    parents.sort(key=lambda tup: tup[1], reverse=False)
    for parent in parents:
        roleta.append(current_probability + (parent[1]/total_fitness)) 
        current_probability = roleta[-1]
    first_parent_id = spin_wheel(roleta, random.random())
    selected_parents.append(parents[first_parent_id])
    second_parent_id =spin_wheel(roleta, random.random())
    selected_parents.append(parents[second_parent_id])
    while(first_parent_id == second_parent_id):
        second_parent_id =spin_wheel(roleta, random.random())
        selected_parents[1] = parents[second_parent_id]    

    return list(map(lambda tup: tup[0], selected_parents)) #2 parents
    
    
def survival_selection(population, parents):
    checksum = 0
    population.sort(key=lambda tup: tup[1], reverse=True)
    for parent in parents:
        for i in range(len(population)):
            if parent == population[i][0]:
                population.pop(i)
                checksum += 1
                break
    if checksum != 2:
        return population[:-1]
    return population

def init_population(population_size):
    population = []
    while population_size > 0:
        population.append(generate_child())
        population_size -= 1
    return population

def generate_child():
    child = [0,1,2,3,4,5,6,7]
    random.shuffle(child)
    return child

def eval(population_fitness):
    for individual in population_fitness:
        if individual[1] == 1:
            return individual[0]
    
    return None

def main():
    population = init_population(100)
    population_fitness = calculate_fitness(population)
    solution = eval(population_fitness)
    count = 0
    while solution == None and count < 10000:
        parents = parent_selection(population_fitness)
        children = cut_and_crossfill(parents)
        children = list(map(lambda child: mutate(child) if random.random() <= 0.4 else child, children)) 
        children = calculate_fitness(children)
        population_fitness.append(children[0])
        population_fitness.append(children[1])
        population_fitness = survival_selection(population_fitness, parents)
        solution = eval(population_fitness)
        count += 1
    if count == 10000:
        return -1
    else:
        total_converged = len(list(filter(lambda x : x[1] == 1, population_fitness)))
        return (count, total_converged, calculate_mean(population_fitness,1), calculate_std(population_fitness,1))

def calculate_mean(generations, pos):
    return np.mean(list(map(lambda x : x[pos], generations)))

def calculate_std(generations, pos):
    return np.std(list(map(lambda x : x[pos], generations)))

generation_infos = []
for i in range(30):
    generation_infos.append(main())
print("Quantidade de convergências: ", 30 - len(list(filter(lambda x : x[0] == -1, generation_infos))))
print('Media de iterações que o algoritmo convergiu: ', calculate_mean(generation_infos, 0), ' Desvio Padrão das iterações que o algoritmo convergiu :', calculate_std(generation_infos, 0))
print('Média de Indivíduos que convergiram por execução : ', calculate_mean(generation_infos, 1))
print('Media Fitness: ', calculate_mean(generation_infos, 2), ' Desvio Padrão Fitness:', calculate_std(generation_infos, 2))

main()
