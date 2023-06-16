from ga.genetic_algorithm import GeneticAlgorithm
from ga.genetic_operators.recombination import Recombination
from ga.individual import Individual


class Recombination2(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)
        self.crossover_point = 0

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        # TODO
        num_genes = ind1.num_genes
        cut = GeneticAlgorithm.rand.randint(0, num_genes - 1)

        child1 = [-1] * len(ind1.genome)
        child2 = [-1] * len(ind1.genome)

        # Create the first child by copying the segment before the cut from ind1
        # and filling in the remaining genes from ind2
        for i in range(cut):
            child1[i] = ind1.genome[i]
            child2[i] = ind2.genome[i]

        # Fill in the remaining genes in child1 using genes from ind2
        for i in range(len(ind1.genome)):
            if ind2.genome[i] not in child1:
                child1[child1.index(-1)] = ind2.genome[i]

        # Fill in the remaining genes in child2 using genes from ind1
        for i in range(len(ind1.genome)):
            if ind1.genome[i] not in child2:
                child2[child2.index(-1)] = ind1.genome[i]

        ind1.genome = child1
        ind2.genome = child2

    def __str__(self):
        return "Recombination 2 (" + f'{self.probability}' + ")"
