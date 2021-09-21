"""
    Assignment 1 : 8 Queens problem using genetic algorithm

    Team Members : Sunny(19234757043), Tanmay (19234757044) 
    
"""

"""
    To Solve 8 Queens Problem using Genetic Algorihtm, below are the steps : 

    1) Representing Individuals (Array in our case whose indexes refers to columns and corresponding
        values refers to rows of board)
    2) Generate initial population randomly
    3) Applying a fitness function
    4) Selecting parents for mating according to fitness scroes
    5) Crossover of parent to produce new generation
    6) Mutation of new generation
    7) Repeat until solution is reached

    Chromosome : It refers to a state in our population or collection of states
    Crossover  : It is mating of two chromosomes to produce a new generation
    Mutation   : It refers to making changes in a chromosome

"""

import random
numofQueens = 8 #solving for 8 Queens
maxFitness = 28 #maximum fitness score that we can achieve

#Generating random chromosomes
def random_chromosome():  
    return [ random.randint(1, numofQueens) for _ in range(numofQueens) ]

#fitness function that returns the fitness score of a chromosome
def fitness(chromosome):
    score = 0    
    for col in range(numofQueens):
        row = chromosome[col]
        
        for other_col in range(numofQueens):
            
            if other_col == col:
                continue
            if chromosome[other_col] == row:
                continue
            if other_col + chromosome[other_col] == col + row:
                continue
            if other_col - chromosome[other_col] == col - row:
                continue
            score += 1 #increment score if pair of queens are non-attacking.
    
    #divide by 2 as (Q1 compared with Q2, then Q2 again compared with Q1 and so on)
    return score/2

def cross_over(chromosome1, chromosome2): 
    n = len(chromosome1)
    ind = random.randint(0, n - 1)  #taking a random index
    return chromosome1[0:ind] + chromosome2[ind:n] #swapping after that index

def mutate(chromosome):
    n = len(chromosome)
    ind = random.randint(0, n - 1)  #taking a random index
    val = random.randint(1, n) #taking a random value
    chromosome[ind] = val  #mutating value at that index
    return chromosome

def probability(chromosome, fitness):
    return fitness(chromosome) / maxFitness

def random_choose(population, probabilities):
    
    population_with_prob = zip(population, probabilities)
    total = sum(probability for chromosome, probability in population_with_prob)
    r = random.uniform(0, total)
    
    initial = 0

    for chromosome, probability in zip(population, probabilities):
        if initial + probability >= r:
            return chromosome
        initial += probability

def print_chromosome(chromosome):
    print("Chromosome = {},  Fitness = {}"
        .format(str(chromosome), fitness(chromosome)))

def print_board(board):
        for row in board:
            print (" ".join(row))
       
def genetic_algo_for_8_queens(population, fitness):
    
    mutation_probability = 0.25
    new_population = []
    probabilities = [probability(n, fitness) for n in population]
    
    for i in range(len(population)):
        
        chromosome1 = random_choose(population, probabilities) #best chromosome 1
        chromosome2 = random_choose(population, probabilities) #best chromosome 2
        
        #Crossover to produce new generation
        child = cross_over(chromosome1, chromosome2) 

        if random.random() < mutation_probability:
            child = mutate(child)
        
        new_population.append(child)

        if fitness(child) == maxFitness: break  #if we have reached to the solution

    return new_population

if __name__ == "__main__":

    #generating initial population
    population = [random_chromosome() for _ in range(100)]   

    #Repeat until solution is reached
    while not maxFitness in [fitness(chromosome) for chromosome in population]:
        population = genetic_algo_for_8_queens(population, fitness)

    output = []

    for chromosome in population:
        if fitness(chromosome) == maxFitness:
            print("");
            print("One of the solutions: ")
            output = chromosome
            print_chromosome(chromosome)
            
    board = []

    for x in range(numofQueens):
        board.append(["-"] * numofQueens)
        
    for i in range(numofQueens):
        board[numofQueens - output[i]][i] = "Q"

    print_board(board)