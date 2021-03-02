import random
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

def order(child, parent1,parent2,cut_point):
    index = (cut_point[1]+1)%8
    index2 = index
    child[cut_point[0]:index] = parent1[cut_point[0]:index]
    while(child.count(-1) > 0):
        if not(parent2[index] in child):
            child[index2] = parent2[index]
            index2 = (index2 + 1)%8
        index= (index + 1)%8
    return child

def first_order_crossover(parents):
    if random.random() <= 0.9:
        parent1 = parents[0]
        parent2 = parents[1]
        cut_point = []
        cut_point.append(random.randint(0,7))
        cut_point.append(random.randint(0,7))
        while(abs(cut_point[1]-cut_point[0])  == 7):
            cut_point[1] = random.randint(0,7)
        cut_point.sort()
        child1 =[-1 for i in range(8)]
        child2 =[-1 for i in range(8)]
        child1 = order(child1,parent1,parent2 ,cut_point)
        child2 = order(child2,parent2, parent1, cut_point)
        
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
    selected_parents.append(parents[spin_wheel(roleta, random.random())])
    selected_parents.append(parents[spin_wheel(roleta, random.random())])
    count = 0
    while(selected_parents[1] == selected_parents[0] and count < 100):
        selected_parents[1] = parents[spin_wheel(roleta, random.random())]
        count +=1         

    return list(map(lambda tup: tup[0], selected_parents)) #2 parents
    
    
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
    return child

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
        children = first_order_crossover(parents)
        children = list(map(lambda child: mutate(child) if random.random() <= 0.4 else child, children)) 
        children = calculate_fitness(children)
        population_fitness.append(children[0])
        population_fitness.append(children[1])
        population_fitness = survival_selection(population_fitness)
        solution = eval(population_fitness)
        count += 1
    print(f'Generation {count}: {solution}')

main()
