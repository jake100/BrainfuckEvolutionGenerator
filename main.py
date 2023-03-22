import random

# Set the target program to evolve towards
target_program = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."

# Define the possible Brainfuck characters to use in the program
bf_chars = "+-><.,[]"

# Set the maximum length of the program and the population size
max_program_length = len(target_program)
population_size = 100

# Define the fitness function
def fitness(program):
    """
    Calculates the fitness of a program by comparing it to the target program.
    """
    score = 0
    for i in range(len(target_program)):
        if program[i] == target_program[i]:
            score += 1
    return score / len(target_program)

# Define the crossover function
def crossover(parent1, parent2):
    """
    Creates a new program by randomly selecting characters from the two parent programs.
    """
    child = ""
    for i in range(len(parent1)):
        if random.random() < 0.5:
            child += parent1[i]
        else:
            child += parent2[i]
    return child

# Define the mutation function
def mutate(program, mutation_rate):
    """
    Mutates the program by randomly changing some of the characters.
    """
    new_program = ""
    for char in program:
        if random.random() < mutation_rate:
            new_program += random.choice(bf_chars)
        else:
            new_program += char
    return new_program

# Generate an initial population of random programs
population = ["".join(random.choices(bf_chars, k=max_program_length)) for i in range(population_size)]

# Evolve the population for a certain number of generations
num_generations = 100
mutation_rate = 0.01
for generation in range(num_generations):
    # Evaluate the fitness of each program
    fitness_scores = [fitness(program) for program in population]

    # Select the parents for the next generation
    parents = []
    for i in range(2):
        parent_index = fitness_scores.index(max(fitness_scores))
        parents.append(population[parent_index])
        del fitness_scores[parent_index]
        del population[parent_index]

    # Create the next generation by crossover and mutation
    next_generation = []
    for i in range(population_size - 2):
        child = crossover(random.choice(parents), random.choice(parents))
        child = mutate(child, mutation_rate)
        next_generation.append(child)

    # Add the parents back into the population
    next_generation.extend(parents)

    # Update the population for the next generation
    population = next_generation

    # Print the best program for this generation
    best_program = max(population, key=fitness)
    print(f"Generation {generation}: {best_program}")