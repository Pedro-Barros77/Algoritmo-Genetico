import numpy as np
import random

def sum_values(_list):
    return sum(_list)
    
def create_population(min_gene_value, max_gene_value,population_size,gene_size,):
    population = np.random.randint(min_gene_value, max_gene_value, (population_size, gene_size))
    return population.tolist()

def get_best_chromosomes(population, min_value):
    target_values = [x for x in population if sum(x) >= min_value]
    return target_values

def get_best_scores(percentage, population):
    population.sort(key = sum_values, reverse=True)
    count = int(len(population) * percentage)
    chosen_parents = population[:count]    
    return chosen_parents

def mutation(chance, population,min_gene_value, max_gene_value):
    mutateds = []
        
    GENE_SIZE = len(population[0])-1
    for c in population:
        value = random.randint(1,100)
        if value > chance * 100:
            continue
        rand_index = random.randint(0,GENE_SIZE)
        rand_value = random.randint(min_gene_value,max_gene_value)
        c[rand_index] = rand_value
        mutateds.append(c)
    return mutateds

def crossover(population, total_population):
    GENE_SIZE = len(population[0])
    j = len(population)
    crossed = []
    while j < total_population:
        rand_index = random.randint(0,len(population)-1)
        split_index = random.randint(1, GENE_SIZE - 1)

        split_1 = [population[rand_index][i:i + split_index] for i in range(0, GENE_SIZE, split_index)]
        half_A1 = split_1[0]
        half_A2 = population[rand_index][len(half_A1):]
        
        available_list = population[:]

        available_list.pop(rand_index)  
        rand_index = random.randint(0,len(available_list)-1)
        
        split_2 = [available_list[rand_index][i:i + split_index] for i in range(0, GENE_SIZE, split_index)]
        half_B1 = split_2[0]
        half_B2 = population[rand_index][len(half_B1):]
        
        c1 = half_A1 + half_B2
        c2 = half_B1 + half_A2
        crossed.append(c1)
        j+=1
        if j >= total_population:
            continue
        crossed.append(c2)
        j+=1
    
    return crossed