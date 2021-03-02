import random
import numpy as np

def calculate_fitness(population):
    result = []
    fenotype_list = list(map(genotype_to_fenotype, population))
    for fenotype in fenotype_list:
        penalty = 1
        for idx, element in enumerate(fenotype):
            for idx2, el in enumerate(fenotype):
                penalty += 1 if (idx != idx2 and abs(idx - idx2) == abs(element - el)) else 0
        result.append((fenotype_to_genotype(fenotype), 1/penalty))
    return result

def genotype_to_fenotype(genotype):
    actual = 0
    fenotype = []
    for i in range(3, len(genotype)+3, 3):
        fenotype.append(int(genotype[(actual*3):i],2))
        actual += 1

    return fenotype


def fenotype_to_genotype(fenotype):
    def add_zeros(element):
        missing = len(element)
        return (3-missing)*'0' + element
    
    return ''.join(map(add_zeros, map(lambda x: "{0:b}".format(x), fenotype)))

def crossfill(child, parent,cut_point):
    index = cut_point
    while(len(child) < 8):
        if not(parent[index] in child):
            child.append(parent[index])
        index= (index + 1)%8
    return child

def cut_and_crossfill(parents):
    if random.random() <= 0.9:
        fenotype_parent1 = genotype_to_fenotype(parents[0])
        fenotype_parent2 = genotype_to_fenotype(parents[1])
        cut_point = random.randint(0,6)

        child1 = fenotype_parent1[0:cut_point]
        child2 = fenotype_parent2[0:cut_point]
        child1 = crossfill(child1,fenotype_parent2,cut_point)
        child2 = crossfill(child2,fenotype_parent1,cut_point)
        child1 = fenotype_to_genotype(child1)
        child2 = fenotype_to_genotype(child2)
    else:
        child1 = parents[0]
        child2 = parents[1]

    return [child1,child2]

def mutate(child):
   fenotype_child = genotype_to_fenotype(child)
   position1 = random.randint(0,7)
   position2 = random.randint(0,7)
   while position1 == position2:
        position1 = random.randint(0,7)
        position2 = random.randint(0,7)
   fenotype_child[position1], fenotype_child[position2] = fenotype_child[position2], fenotype_child[position1]
   return fenotype_to_genotype(fenotype_child)

def parent_selection(population):
    parents = select_random_parents(population)
    parents.sort(key=lambda tup: tup[1], reverse=True)
    selected_parents = parents[0:2]
    return list(map(lambda tup: tup[0], selected_parents)) #2 parents

def select_random_parents(population):
    random_parents = []
    for i in range(5):
        random_parents.append(population[random.randint(0,9)])
    return random_parents
    
def survival_selection(population):
    population.sort(key=lambda tup: tup[1], reverse=True)
    return population[:-2]

def init_population(population_size):
    population = []
    while population_size > 0:
        population.append(generate_child())
        population_size -= 1
    return population

def generate_child():
    child = [0,1,2,3,4,5,6,7]
    random.shuffle(child)
    return fenotype_to_genotype(child)

def eval(population_fitness):
    for individual in population_fitness:
        if individual[1] == 1:
            return individual[0]
    
    return None

def main():
    population = init_population(10)
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
        population_fitness = survival_selection(population_fitness)
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
