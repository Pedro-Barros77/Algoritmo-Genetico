from datetime import datetime
from time import sleep
import backend.methods as md
from PyQt5.QtCore import pyqtSignal, QThread

def print_c(text, color, br = True):
    print(f"\033[{color}m{text}", end="\n" if br == True else "")

class GeneticAlgorithm(QThread):

    resultAvailable = pyqtSignal(object)
    startup_callback = pyqtSignal(object)
    colocation_callback = pyqtSignal(object)
    podium = []
    data = {
            'generations': 1,
            'bestscore': 0,
            'mutations': 0,
            'perfect_value': 0,
            'minimal_value': 0, 
            'worst_score': 0,
            'succeeded_count':0,
            'is_Alive' : True
        }
    
    def __init__(self, input_values):
        QThread.__init__(self)
        self.input_values = input_values
        self.alive = True
    def stop(self):
        self.alive = False
        self.data['is_Alive'] = False
        self.wait()

    def run(self):    
        BLUE = 34
        WHITE = 97
        L_BLUE = 36
        GREEN = 32 
        YELLOW = 33

        self.podium.clear()
        self.data.clear()      
       

        START_TIME = datetime.now()
        print_c(f"\nProcesso iniciado em: {START_TIME.strftime('%H:%M:%S:%f')}", BLUE)

        TOTAL_POPULATION = self.input_values['population']
        TOTAL_GENES = self.input_values['total_genes']
        MIN_GENE_VALUE = self.input_values['min_genes']
        MAX_GENE_VALUE = self.input_values['max_genes']
        TARGET_PERCENTAGE = self.input_values['target_perc']
        MIN_SUCCEEDED = self.input_values['min_succeed']
        CHOSEN_PERCENTAGE = self.input_values['chosen_perc']
        MUTATION_PERCENTAGE = self.input_values['mutation_perc'] 

        

        if int(TOTAL_POPULATION * CHOSEN_PERCENTAGE) <= 1:
            print(f"O número de escolhidos não pode ser menor que 2. ({TOTAL_POPULATION} * {CHOSEN_PERCENTAGE} = {TOTAL_POPULATION * CHOSEN_PERCENTAGE})" )
            return


        MAX_VALUE = (MAX_GENE_VALUE*TOTAL_GENES)
        TARGET_VALUE = int(TARGET_PERCENTAGE * MAX_VALUE)

        start_info = {
            'perfect_value': MAX_VALUE,
            'minimal_value': TARGET_VALUE, 
        }

        self.startup_callback.emit(start_info)

        first_population = md.create_population(MIN_GENE_VALUE,MAX_GENE_VALUE,TOTAL_POPULATION,TOTAL_GENES)
        current_population = first_population
        succeeded_chromosomes = md.get_best_chromosomes(current_population, TARGET_VALUE)
        generations = 1
        mutations = 0
        self.data["bestscore"] = TOTAL_GENES * MIN_GENE_VALUE
        _podium_history = []
        while len(succeeded_chromosomes) < MIN_SUCCEEDED:
            chosen_parents = md.get_best_scores(CHOSEN_PERCENTAGE, current_population)
            
            mutated_population = md.mutation(MUTATION_PERCENTAGE, chosen_parents,MIN_GENE_VALUE,MAX_GENE_VALUE )
            
            crossed_population = md.crossover(chosen_parents, TOTAL_POPULATION - len(mutated_population))
            
            current_population = mutated_population + crossed_population + chosen_parents
        
            succeeded_chromosomes = md.get_best_chromosomes(current_population, TARGET_VALUE)

            _old_podium_count = len(self.podium)
            self.podium = succeeded_chromosomes
            _podium_history += (self.podium[_old_podium_count:])
            # self.podium.sort(key = md.sum_values, reverse=True)
                
            if len(self.podium)>_old_podium_count:
                self.colocation_callback.emit(_podium_history)
                

            bestscore = sum(max(current_population))
            worst_score = sum(min(current_population))

            generations +=1
            mutations += len(mutated_population)
            
            self.data["generations"] = generations
            self.data["mutations"] = mutations
            self.data["bestscore"] = bestscore
            self.data["worst_score"] = worst_score
            self.data["succeeded_count"] = len(succeeded_chromosomes)
            self.data["is_Alive"] = self.alive
            self.resultAvailable.emit(self.data)
            
            if not self.alive:
                break
            sleep(0.01)
        
        END_TIME = datetime.now()
        TIME_ELAPSED = END_TIME - START_TIME
        print_c(f"Processo finalizado, tempo decorrido: {TIME_ELAPSED}", BLUE)
        # print_c("Valor mínimo esperado: ", WHITE, False)
        # print_c(TARGET_VALUE, L_BLUE, False)
        # print_c(" Valor ideal (perfeito): ", WHITE, False)
        # print_c(MAX_VALUE, GREEN)
        
        # print_c("Houve ", WHITE, False)
        # print_c(generations, L_BLUE, False)
        # print_c(" gerações, ", WHITE, False)
        # print_c(mutations, YELLOW, False)
        # print_c(" mutações. Cromossomos sucedidos (", WHITE, False)
        # print_c(len(succeeded_chromosomes), GREEN, False)
        # print_c("): ", WHITE)
        # for chro in succeeded_chromosomes:
        #     print_c(f"{chro} = ", WHITE, False)
        #     print_c(sum(chro), GREEN)
        # print_c("", WHITE)




#Criado por Pedro Barros (github.com/Pedro-Barros77) 
#e Elias Lima (github.com/Elias-Lima-code)
#(UNA - 'Sistemas de Informação' e 'Gestão de Tecnologia da Informação')
#para fins de prática e estudos em Inteligência Artificial,
#Primeira versão em 24-09-2022

#Uso e implementação livre, favor incluir os devidos créditos