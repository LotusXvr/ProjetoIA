from ga.genetic_algorithm import GeneticAlgorithm
from ga.genetic_operators.recombination import Recombination
from ga.individual import Individual
import numpy as np

class Recombination3(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)
        self.crossover_point = 0

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        num_genes = ind1.num_genes
        cut1 = GeneticAlgorithm.rand.randint(0, num_genes - 1)
        cut2 = GeneticAlgorithm.rand.randint(0, num_genes - 1)
        if cut2 < cut1:
            cut1, cut2 = cut2, cut1

        child1 = [-1] * len(ind1.genome)
        child2 = [-1] * len(ind1.genome)

        # Create the first child by copying the segment between cut1 and cut2 from ind1
        for i in range(cut1, cut2 + 1):
            child1[i] = ind1.genome[i]

        # Fill in the remaining genes in child1 using genes from ind2
        for i in range(len(ind1.genome)):
            if i < cut1 or i > cut2:
                gene = ind2.genome[i]
                while gene in child1:
                    indices = np.where(ind1.genome == gene)[0]
                    gene = ind2.genome[indices[0]]
                child1[i] = gene

        # Create the second child by copying the segment between cut1 and cut2 from ind2
        for i in range(cut1, cut2 + 1):
            child2[i] = ind2.genome[i]

        # Fill in the remaining genes in child2 using genes from ind1
        for i in range(len(ind1.genome)):
            if i < cut1 or i > cut2:
                gene = ind1.genome[i]
                while gene in child2:
                    indices = np.where(ind2.genome == gene)[0]
                    gene = ind1.genome[indices[0]]
                child2[i] = gene

        ind1.genome = child1
        ind2.genome = child2

    def __str__(self):
        return "Recombination 3 (" + f'{self.probability}' + ")"
