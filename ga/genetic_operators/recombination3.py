from ga.genetic_algorithm import GeneticAlgorithm
from ga.genetic_operators.recombination import Recombination
from ga.individual import Individual


class Recombination3(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)
        self.crossover_point = 0

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        # TODO
        for i in range(len(ind1)):
            if GeneticAlgorithm.rand.random() < 0.5:
                ind1.genome[i], ind2.genome[i] = ind2.genome[i], ind1.genome[i]
        pass

    def __str__(self):
        return "Recombination 3 (" + f'{self.probability}' + ")"
