import random
import copy
import matplotlib.pyplot as plt

N = 50
P = 50
MUTRATE = 0.01
Generations = 100

average_fitness_list = []
best_fitness_list = []

class individual: 
    def __init__(self):
        self.gene = [0]*N   
        self.fitness = 0  

population = [] 

for x in range (0, P):
    tempgene=[]
    for y in range (0, N):
        tempgene.append( random.randint(0,1))
    newind = individual()
    newind.gene = tempgene.copy()
    population.append(newind)
        
        
def test_function( ind ):
    utility=0
    for i in range(N):
        utility = utility + ind.gene[i]
    return utility

for ind in population:
    ind.fitness = test_function(ind) 
        
for x in range(Generations): 
    offspring = []
    for i in range (0, P):
        parent1 = random.randint( 0, P-1 )
        off1 = copy.deepcopy(population[parent1])
        parent2 = random.randint( 0, P-1 )
        off2 = copy.deepcopy(population[parent2])
        if off1.fitness > off2.fitness:
            offspring.append( off1 )
        else:
            offspring.append( off2 )

    toff1 = individual()
    toff2 = individual()
    temp = individual()
    for i in range( 0, P, 2 ):
        toff1 = copy.deepcopy(offspring[i])
        toff2 = copy.deepcopy(offspring[i+1])
        temp = copy.deepcopy(offspring[i])
        crosspoint = random.randint(1,N)
        for j in range (crosspoint, N):
            toff1.gene[j] = toff2.gene[j]
            toff2.gene[j] = temp.gene[j]
        offspring[i] = copy.deepcopy(toff1)
        offspring[i+1] = copy.deepcopy(toff2)
        


    new_offspring = []

    for i in range(0, P):
        newind = individual();
        newind.gene = []
        for j in range(0, N):
            gene = offspring[i].gene[j]
            mutprob = random.random()
            if mutprob < MUTRATE:
                if gene == 1:
                    gene = 0
                else:
                    gene = 1
            newind.gene.append(gene)
        new_offspring.append(newind)

    
    for newind in new_offspring:
        newind.fitness = test_function(newind) 
        
    population = copy.deepcopy(new_offspring)


    average_fitness = sum(ind.fitness for ind in population) / P


    best_individual = max(population, key=lambda ind: ind.fitness)
    
    average_fitness_list.append(average_fitness)
    best_fitness_list.append(best_individual.fitness)
    
    print("Average population fitness:", average_fitness)
    print("Best population fitness:", best_individual.fitness)
    print("\n")
    
plt.plot(range(Generations), average_fitness_list, label='Average Fitness')
plt.plot(range(Generations), best_fitness_list, label='Best Fitness')
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.legend()
plt.show()
