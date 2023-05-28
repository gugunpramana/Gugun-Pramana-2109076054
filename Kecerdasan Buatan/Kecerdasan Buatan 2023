import random
import math

# Fungsi evaluasi
def evaluate_chromosome(chromosome):
    a = chromosome[0]
    b = chromosome[1]
    c = chromosome[2]
    d = chromosome[3]
    equation_result = a + 4*b + 2*c + 3*d
    objective_value = abs(equation_result - 30)
    return objective_value

# Inisialisasi populasi
def initialize_population(pop_size):
    population = []
    for _ in range(pop_size):
        chromosome = [random.randint(0, 30), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)]
        population.append(chromosome)
    return population

# Seleksi orang tua menggunakan metode Roulette Wheel Selection
def roulette_wheel_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    probabilities = [fitness/total_fitness for fitness in fitness_values]
    cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]

    r = random.uniform(0, 1)
    for i in range(len(cumulative_probabilities)):
        if r < cumulative_probabilities[i]:
            return population[i]

# Operasi crossover menggunakan one-cut point crossover
def crossover(parent1, parent2):
    cut_point = random.randint(1, 3)
    child1 = parent1[:cut_point] + parent2[cut_point:]
    child2 = parent2[:cut_point] + parent1[cut_point:]
    return child1, child2

# Operasi mutasi
def mutation(chromosome, mutation_rate):
    mutated_chromosome = chromosome.copy()
    for i in range(len(mutated_chromosome)):
        if random.uniform(0, 1) < mutation_rate:
            if i == 0:
                mutated_chromosome[i] = random.randint(0, 30)
            else:
                mutated_chromosome[i] = random.randint(0, 10)
    return mutated_chromosome

# Algoritma Genetika
def genetic_algorithm(pop_size, max_gen, crossover_rate, mutation_rate):
    population = initialize_population(pop_size)
    best_chromosome = None

    for gen in range(max_gen):
        fitness_values = [1 / (1 + evaluate_chromosome(chromosome)) for chromosome in population]
        best_fitness = max(fitness_values)
        best_index = fitness_values.index(best_fitness)
        best_chromosome = population[best_index]

        new_population = []
        for _ in range(pop_size // 2):
            parent1 = roulette_wheel_selection(population, fitness_values)
            parent2 = roulette_wheel_selection(population, fitness_values)

            if random.uniform(0, 1) < crossover_rate:
                child1, child2 = crossover(parent1, parent2)
            else:
                child1, child2 = parent1, parent2

            child1 = mutation(child1, mutation_rate)
            child2 = mutation(child2, mutation_rate)

            new_population.append(child1)
            new_population.append(child2)

        population = new_population

    return best_chromosome

# Main program
population_size = 6
max_generation = 100
crossover_rate = 0.8
mutation_rate = 0.1

best_solution = genetic_algorithm(population_size, max_generation, crossover_rate, mutation_rate)
print("Best solution found: ", best_solution)
