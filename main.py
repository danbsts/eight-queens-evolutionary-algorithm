import random

def calculate_fitness(population):
    result = []
    fenotype_list = list(map(genotype_to_fenotype, population))
    for fenotype in fenotype_list:
        penalty = 1
        for idx, element in enumerate(fenotype):
            for idx2, el in enumerate(fenotype):
                penalty += 1 if (idx != idx2 and abs(idx - idx2) == abs(element - el)) else 0
        result.append((fenotype, 1/penalty))
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

def cut_and_crossfill(parent1, parent2):
    fenotype_parent1 = genotype_to_fenotype(parent1)
    fenotype_parent2 = genotype_to_fenotype(parent2)
    print(fenotype_parent1)
    print(fenotype_parent2)
    cut_point = random.randint(0,6)

    child1 = fenotype_parent1[0:cut_point]
    child2 = fenotype_parent2[0:cut_point]
    child1 = crossfill(child1,fenotype_parent2,cut_point)
    child2 = crossfill(child2,fenotype_parent1,cut_point)
    print(child1)
    print(child2)
    child1 = fenotype_to_genotype(child1)
    child2 = fenotype_to_genotype(child2)

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
    selected_parents = parents[0:2]
    return selected_parents #2 parents

def select_random_parents(population):
    random_parents = []
    for i in range(5):
        random_parents.append(population[random.randint(0,100)])
    return random_parents
    
def survival_selection(population):
    population.sort(key=lambda tup: -tup[1])
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
    population = init_population(100)
    population_fitness = calculate_fitness(population)
    solution = eval(population_fitness)
    count = 0
    while solution == None and count < 2:
      count += 1
    print(solution)

main()
