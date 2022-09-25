import numpy as np
import random

def sum_values(_list):
    return sum(_list)

#Cria a população inicial, contendo x individuos com y genes em cada
def create_population(MIM_GENE_VALUE, MAX_GENE_VALUE,population_size,gene_size,):

    population = np.random.randint(MIM_GENE_VALUE,MAX_GENE_VALUE, (population_size, gene_size))
    return population.tolist()

#retorna os individuos da população que tingiram valor mínimo da soma dos genes
def get_best_chromosomes(population, min_value):
    target_values = [x for x in population if sum(x) >= min_value]
    return target_values

#Define os cromossomos com as melhores pontuações, escolhendo 
#uma quantidade com base na porcentagem
def get_best_scores(percentage, population):
    population.sort(key = sum_values, reverse=True)
    count = int(len(population) * percentage)
    chosen_parents = population[slice(count)]
    return chosen_parents
    
# Operador genético que escolhe aleatoriamente um indivíduo, seleciona um ponto aleatório
# em seus genes e os divide em 2 (A1 e A2). Um outro indivíduo é selecionado e também dividido (B1 e B2).
# Ocorre então o cruzamento dos genes, onde 2 novos indivíduos são gerados: A1+B2 e B1+A2
def crossover(population, TOTAL_POPULATION):
    GENE_SIZE = len(population[0])
    j = len(population)
    while j < TOTAL_POPULATION:
        rand_index = random.randint(0,len(population)-1)
        split_index = random.randint(1, GENE_SIZE - 1)

        split_1 = [population[rand_index][i:i + split_index] for i in range(0, GENE_SIZE, split_index)]
        half_A1 = split_1[0]
        half_A2 = population[rand_index][len(half_A1):]
        
        available_list = list(population)
        available_list.remove(population[rand_index])
        rand_index = random.randint(0,len(available_list)-1)
        
        split_2 = [available_list[rand_index][i:i + split_index] for i in range(0, GENE_SIZE, split_index)]
        half_B1 = split_2[0]
        half_B2 = population[rand_index][len(half_B1):]
        
        c1 = half_A1 + half_B2
        c2 = half_B1 + half_A2
        
        population.append(c1)
        j+=1
        if j >= TOTAL_POPULATION:
            continue
        population.append(c2)
        j+=1
    return population

# Operador genético que escolhe um gene aleatório do cromossomo e altera
# o valor aleatoriamente
def mutation(chance, population,MIM_GENE_VALUE, MAX_GENE_VALUE):
    mutateds = []
        
    GENE_SIZE = len(population[0])-1
    for c in population:
        value = random.randint(1,100)
        if value > chance * 100:
            continue
        rand_index = random.randint(0,GENE_SIZE)
        rand_value = random.randint(MIM_GENE_VALUE,MAX_GENE_VALUE)
        c[rand_index] = rand_value
        mutateds.append(c)
    return mutateds