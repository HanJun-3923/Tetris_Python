from GameCostCalculator import GameCostCalculator
import random
from Player import AIPlayer

class GeneticAlgorithm:
    population_size = 20
    mutation_rate = 0.1
    crossover_rate = 0.8
    generations = 50

    def __init__(self, Player:AIPlayer):
        self.population = []
        self.fitness = []
        self.player = Player

    def initialize_population(self):
        for _ in range(self.population_size):
            individual = [
                random.uniform(-100, 100),  # heightWeight
                
                random.uniform(-100, 100),  # makeHoleWeight for 1 deep
                random.uniform(-100, 100),  # makeHoleWeight for 2 deep
                random.uniform(-100, 100),  # makeHoleWeight for 3 deep
                random.uniform(-100, 100),  # makeHoleWeight for 4 deep
                random.uniform(-100, 100),  # makeHoleWeight for 5 deep
                
                random.uniform(-100, 100),  # clearLineWeight for 0 index
                random.uniform(-100, 100),  # clearLineWeight for 1 index
                random.uniform(-100, 100),  # clearLineWeight for 2 index
                random.uniform(-100, 100),  # clearLineWeight for 3 index
                random.uniform(-100, 100)   # clearLineWeight for 4 index
            ]
            self.population.append(individual)

    def calculate_fitness(self):
        self.fitness = []
        for individual in self.population:
            # Create an instance of GameCostCalculator with the individual's weights
            gameCostCalculator = GameCostCalculator(self.player.mainTable, self.player.block.crntBlockShape)
            gameCostCalculator.heightWeight = individual[0]
            gameCostCalculator.makeHoleWeight = individual[1:6]
            gameCostCalculator.clearLineWeight = individual[6:11]

            # Calculate the cost and append it to the fitness list
            self.player.startAutoPlace(0.00001)
            if self.player.isGameOver:
                
                pass
            cost = gameCostCalculator.getCost()
            self.fitness.append([cost, gameCostCalculator])

    def selection(self):
        # Perform selection based on fitness
        # (You can choose the selection strategy of your choice)
        pass

    def crossover(self):
        # Perform crossover to create new offspring
        # (You can choose the crossover strategy of your choice)
        pass

    def mutation(self):
        # Perform mutation on the offspring
        # (You can choose the mutation strategy of your choice)
        pass

    def evolve(self):
        self.initialize_population()
        for _ in range(self.generations):
            self.calculate_fitness()
            self.selection()
            self.crossover()
            self.mutation()

        # Get the best individual from the final population
        best_individual = self.population[self.fitness.index(max(self.fitness))]
        return best_individual

if __name__ == "__main__":
    aiPlayer = AIPlayer(2)
    geneticAlgorithm = GeneticAlgorithm(aiPlayer)
    geneticAlgorithm.evolve()
    