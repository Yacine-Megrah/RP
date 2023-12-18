import random



# Chromosome class
class Chromosome:
    def __init__(self, genes=None):
        if genes is None:
            genes = [random.randint(1, 8) for _ in range(63)]
        self.genes = genes

    def crossover(self, partner):
        crossover_point = random.randint(1, 62)
        offspring1_genes = self.genes[:crossover_point] + partner.genes[crossover_point:]
        offspring2_genes = partner.genes[:crossover_point] + self.genes[crossover_point:]
        return Chromosome(offspring1_genes), Chromosome(offspring2_genes)

    def mutation(self, mutation_probability):
        for i in range(len(self.genes)):
            if random.random() < mutation_probability:
                self.genes[i] = random.randint(1, 8)

# Knight class
class Knight:
    def __init__(self, chromosome=None):
        if chromosome is None:
            chromosome = Chromosome()
        self.position = start_pos #(0,0)
        self.chromosome = chromosome
        self.path = [self.position]
        self.fitness = 0

    def move_forward(self, direction):
        # Implement move logic based on direction and update self.position
        new_position = (
            self.position[0] + moves[direction - 1][0],
            self.position[1] + moves[direction - 1][1])
        if(0 <= new_position[0] <= 7 and 0 <= new_position[1] <= 7):
            self.position = new_position

    def move_backward(self, direction):
        # Reverse the move_forward operation and update self.position
        new_position = (
            self.position[0] - moves[direction - 1][0],
            self.position[1] - moves[direction - 1][1])
        self.position = new_position

    def check_moves(self):
        for move in self.chromosome.genes:
            # Apply move_forward and check validity. If invalid, use move_backward and cycle through remaining moves.
            # Update self.path accordingly.
            self.move_forward(move)
            self.path.append(self.position)
            if(not (0 <= self.position[0] <= 7)) or (not(0 <= self.position[1] <= 7)):
                self.move_backward(move)
                self.path.pop()

    def evaluate_fitness(self):
        self.fitness = 64 - len(set(self.path))
        if self.fitness == 64:
            # Optimal solution found!
            # add to elite
            elite.append(self)
        return self.fitness

# Population class
class Population:
    def __init__(self, population_size):
        self.population_size = population_size
        self.generation = 1
        self.knights = [Knight() for _ in range(population_size)]

    def check_population(self):
        for knight in self.knights:
            knight.check_moves()

    def evaluate(self):
        best_knight = None
        highest_fitness = 0
        for knight in self.knights:
            knight.evaluate_fitness()
            if knight.fitness > highest_fitness:
                best_knight = knight
                highest_fitness = knight.fitness
        return best_knight, highest_fitness

    def tournament_selection(self, size):
        gladiator_knights = random.sample(self.knights, size)
        selected_knight1 = Knight()
        selected_knight2 = Knight()
        for knight in gladiator_knights:
            if knight.fitness > selected_knight1.fitness:
                selected_knight1 = knight
            elif knight.fitness > selected_knight2.fitness:
                selected_knight2 = knight
        return selected_knight1, selected_knight2

    def create_new_generation(self):
        new_knights = []
        for _ in range(self.population_size):
            parent1, parent2 = self.tournament_selection(3)
            offspring1, offspring2 = parent1.chromosome.crossover(parent2.chromosome)
            offspring1.mutation(mutation_probability)
            offspring2.mutation(mutation_probability)
            new_knights.append(Knight(offspring1))
            new_knights.append(Knight(offspring2))
        self.knights = new_knights
        self.generation += 1

start_pos = (4,3)
population_size = 50
mutation_probability = 0.05
max_generations = 1000
moves = [(-1, 2), (1, 2),
         (-2, 1), (2, 1),
         (-2, -1), (2, -1),
         (-1, -2), (1, -2)]

elite = []

def knights_tour():
    best_eval = 0
    best_run = []
    population = Population(population_size)    

    for _ in range(max_generations):

        population.check_population()
        best_knight, highest_fitness = population.evaluate()

        # print(f"Generation {_}, evaluation: {highest_fitness}")
        # print(f"best Knight start: {best_knight.path}.")

        if highest_fitness > best_eval:
            best_run = best_knight.path
        if highest_fitness == 64:
            break
        population.create_new_generation()
    return best_run