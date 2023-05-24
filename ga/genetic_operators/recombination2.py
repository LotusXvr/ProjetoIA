from ga.genetic_operators.recombination import Recombination
from ga.individual import Individual


class Recombination2(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)
        self.crossover_point = 0

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        # TODO
        self.crossover_point = int(len(ind1.genome) / 2)
        ind1.genome, ind2.genome = ind1.genome[:self.crossover_point] + ind2.genome[self.crossover_point:], \
                                   ind2.genome[:self.crossover_point] + ind1.genome[self.crossover_point:]

    def __str__(self):
        return "Recombination 2 (" + f'{self.probability}' + ")"
