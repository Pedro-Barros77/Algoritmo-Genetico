from datetime import datetime
import methods as md

# Imprime no console na cor escolhida
def print_c(text, color, br = True):
    print(f"\033[{color}m{text}", end="\n" if br == True else "")

#função principal onde acontece a lógica do algoritmo genético
def main():
    #region Color Mapping
    BLUE = 34
    WHITE = 97
    L_BLUE = 36
    GREEN = 32 
    YELLOW = 33
    #endregion
    
    START_TIME = datetime.now()
    print_c(f"\nProcesso iniciado em: {START_TIME.strftime('%H:%M:%S:%f')}", BLUE)
    
    TOTAL_POPULATION = 50
    TOTAL_GENES = 5
    TARGET_PERCENTAGE = 0.98
    CHOSEN_PERCENTAGE = 0.3
    MUTATION_PERCENTAGE = 0.01
    MIN_SUCCEEDED = 1
    
    MAX_VALUE = (9*TOTAL_GENES)
    TARGET_VALUE = int(TARGET_PERCENTAGE * MAX_VALUE)
    
    first_population = md.create_population(TOTAL_POPULATION,TOTAL_GENES)
    succeeded_chromosomes = md.get_best_chromosomes(first_population, TARGET_VALUE)
    
    _generations = 1
    _mutations = 0
    while len(succeeded_chromosomes) < MIN_SUCCEEDED:
        chosen_parents = md.get_best_scores(CHOSEN_PERCENTAGE, first_population)
        mutated_population = md.mutation(MUTATION_PERCENTAGE, chosen_parents)
        crossed_population = md.crossover(chosen_parents, TOTAL_POPULATION if not mutated_population else (TOTAL_POPULATION - len(mutated_population)))
        new_population = crossed_population if not mutated_population else mutated_population + crossed_population
        succeeded_chromosomes = md.get_best_chromosomes(new_population, TARGET_VALUE)
        _generations +=1
        if mutated_population:
            _mutations += 1
    
    END_TIME = datetime.now()
    TIME_ELAPSED = END_TIME - START_TIME
    print_c(f"Processo finalizado, tempo decorrido: {TIME_ELAPSED}", BLUE)
    print_c("Valor mínimo esperado: ", WHITE, False)
    print_c(TARGET_VALUE, L_BLUE, False)
    print_c(" Valor ideal (perfeito): ", WHITE, False)
    print_c(MAX_VALUE, GREEN)
    
    print_c("Houve ", WHITE, False)
    print_c(_generations, L_BLUE, False)
    print_c(" gerações, ", WHITE, False)
    print_c(_mutations, YELLOW, False)
    print_c(" mutações. Cromossomos sucedidos (", WHITE, False)
    print_c(len(succeeded_chromosomes), GREEN, False)
    print_c("): ", WHITE)
    for chro in succeeded_chromosomes:
        print_c(f"{chro} = ", WHITE, False)
        print_c(sum(chro), GREEN)
    print_c("", WHITE)
        
main()


#Criado por Pedro Barros (github.com/Pedro-Barros77) 
#e Elias Lima (github.com/Elias-Lima-code)
#(UNA - 'Sistemas de Informação' e 'Gestão de Tecnologia da Informação')
#para fins de prática e estudos em Inteligência Artificial,
#Primeira versão em 24-09-2022

#Uso e implementação livre, favor incluir os devidos créditos