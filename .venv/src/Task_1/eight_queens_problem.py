import random
import time


class EightQueensProblem:
    def __init__(self, transition_model, initial_state: [int] = None):
        self.initial_state: [int] = initial_state or [random.randint(0, 7) for i in range(8)]
        self.state: [int] = self.initial_state.copy()
        self.transition_model = transition_model
        if transition_model == "genetic":
            self.genetic_algorithm([self.generate_random_individual() for i in range(20)])

    def heuristic(self, state):
        attacks = 0
        for i in range(8):
            for j in range(i + 1, 8):
                if state[i] == state[j] or \
                        state[i] - i == state[j] - j or \
                        state[i] + i == state[j] + j:
                    attacks += 1
        return attacks

    def print_state(self, state):
        print("________________")
        line = ""
        for i in range(8):
            for index, queen in enumerate(state):
                if queen == i:
                    line += "|Q"
                elif (i % 2 == 0 and index % 2 == 0) or (i % 2 == 1 and index % 2 == 1):
                    line += "|_"
                else:
                    line += "|#"

            line += "|\n"
        print(line)

    def heuristics_all_actions(self):
        actions = []
        for i in range(8):
            column = []
            for j in range(8):
                new_state = self.state.copy()
                new_state[i] = j
                column.append((new_state, self.heuristic(new_state)))

            actions.append(column)
        return actions

    def print_heuristics_all_actions(self):
        line = ""
        for index, column in enumerate(self.heuristics_all_actions()):
            for state, heuristic in column:
                if state[index] == self.state[index]:
                    line += "|Q "
                else:
                    if heuristic < 10:
                        heuristic = str(heuristic) + str(" ")
                    else:
                        heuristic = str(heuristic)
                    line += "|" + heuristic
            line += "|\n"

        print(line)

    def genetic_algorithm(self, population: []):
        individual_fittest = None
        for j in range(200):
            new_population = []

            for i in range(len(population)):
                x = self.random_selection(population)
                y = self.random_selection(population)
                child = self.reproduce(x, y)
                # Mutate child with 1-5% probability
                if random.random() < random.uniform(0.01, 0.1):
                    child[random.randint(0, 7)] = random.randint(0, 7)
                new_population.append(child)

            population = new_population
            #print(population)
            # Print the best individual in the population based on the fitness function
            population_fitness = self.fitness_function(population)
            print(population_fitness)
            individual_fittest, individual_fittest_fitness, individual_fittest_fitness_perc = max(population_fitness, key=lambda x: x[1])
            print(f"Generation {j}: {individual_fittest} - : {individual_fittest_fitness}")
            # wait 2 seconds
            #time.sleep(2)
            if self.heuristic(individual_fittest) == 0:
                break

        return individual_fittest



    def fitness_function(self, population):
        # Calculate the Fitness of each individual
        fitnesses = [(individual, 28 - self.heuristic(individual)) for individual in population]
        # Calculate total Fitness
        total_fitness = sum(fitness for individual, fitness in fitnesses)
        # Return calculated Probabilities
        return [(individual, fitness, fitness / total_fitness) for individual, fitness in fitnesses]

    def random_selection(self, population):
        probabilities = self.fitness_function(population)
        r = random.random()
        #print("r: ", r)
        sum_probabilities = 0
        # Iterate over the individuals and their probabilities
        for individual, fitness, probability in probabilities:
            sum_probabilities += probability
            #print("sum_probabilities: ", sum_probabilities)
            # If the sum of probabilities is greater than or equal to the random number, return the current individual
            if sum_probabilities >= r:
                return individual

        # If no individual is selected (due to floating point precision issues), return the last individual
        return population[-1]

    def reproduce(self, x, y):
        n = len(x)
        c = random.randint(1, n)
        child = x[:c] + y[c:]
        return child

    def generate_random_individual(self):
        return [random.randint(0, 7) for i in range(8)]

    def generate_unique_individual(self, existing_population):
        while True:
            new_individual = [random.randint(0, 7) for i in range(8)]
            if new_individual not in existing_population:
                return new_individual