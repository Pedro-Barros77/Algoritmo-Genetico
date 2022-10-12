from datetime import datetime
import methods as md
import asyncio

def print_c(text, color, br = True):
    print(f"\033[{color}m{text}", end="\n" if br == True else "")

def main():

    BLUE = 34
    WHITE = 97
    L_BLUE = 36
    GREEN = 32 
    YELLOW = 33

    START_TIME = datetime.now()
    print_c(f"\nProcesso iniciado em: {START_TIME.strftime('%H:%M:%S:%f')}", BLUE)

    TOTAL_POPULATION = 50
    TOTAL_GENES = 5
    TARGET_PERCENTAGE = 0.98
    MIN_GENE_VALUE = 1
    MAX_GENE_VALUE = 9
    MIN_SUCCEEDED = 3
    CHOSEN_PERCENTAGE = 0.3
    MUTATION_PERCENTAGE = 0.01

    

    if int(TOTAL_POPULATION * CHOSEN_PERCENTAGE) <= 1:
        print(f"O número de escolhidos não pode ser menor que 2. ({TOTAL_POPULATION} * {CHOSEN_PERCENTAGE} = {TOTAL_POPULATION * CHOSEN_PERCENTAGE})" )
        return


    MAX_VALUE = (MAX_GENE_VALUE*TOTAL_GENES)
    TARGET_VALUE = int(TARGET_PERCENTAGE * MAX_VALUE)
    print(f"valor max: {MAX_VALUE}\ntarget value {TARGET_VALUE}")
    

    first_population = md.create_population(MIN_GENE_VALUE,MAX_GENE_VALUE,TOTAL_POPULATION,TOTAL_GENES)
    current_population = first_population
    succeeded_chromosomes = md.get_best_chromosomes(current_population, TARGET_VALUE)
    generations = 1
    mutations = 0
    bestscore = TOTAL_GENES * MIN_GENE_VALUE
    
    while len(succeeded_chromosomes) < MIN_SUCCEEDED:
        #15
        chosen_parents = md.get_best_scores(CHOSEN_PERCENTAGE, current_population)
        
        mutated_population = md.mutation(MUTATION_PERCENTAGE, chosen_parents,MIN_GENE_VALUE,MAX_GENE_VALUE )
        
        crossed_population = md.crossover(chosen_parents, TOTAL_POPULATION - len(mutated_population))
        
        current_population = mutated_population + crossed_population + chosen_parents
    
        succeeded_chromosomes = md.get_best_chromosomes(current_population, TARGET_VALUE)
        bestscore = sum(max(current_population))

        generations +=1
        mutations += len(mutated_population)
    
    END_TIME = datetime.now()
    TIME_ELAPSED = END_TIME - START_TIME
    print_c(f"Processo finalizado, tempo decorrido: {TIME_ELAPSED}", BLUE)
    print_c("Valor mínimo esperado: ", WHITE, False)
    print_c(TARGET_VALUE, L_BLUE, False)
    print_c(" Valor ideal (perfeito): ", WHITE, False)
    print_c(MAX_VALUE, GREEN)
    
    print_c("Houve ", WHITE, False)
    print_c(generations, L_BLUE, False)
    print_c(" gerações, ", WHITE, False)
    print_c(mutations, YELLOW, False)
    print_c(" mutações. Cromossomos sucedidos (", WHITE, False)
    print_c(len(succeeded_chromosomes), GREEN, False)
    print_c("): ", WHITE)
    for chro in succeeded_chromosomes:
        print_c(f"{chro} = ", WHITE, False)
        print_c(sum(chro), GREEN)
    print_c("", WHITE)


main()