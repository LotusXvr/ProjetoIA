from ga.genetic_algorithm import GeneticAlgorithm
from ga.genetic_operators.mutation import Mutation
from ga.individual_int_vector import IntVectorIndividual
import numpy as np

class Mutation2(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        num_genes = len(ind.genome)
        cut = GeneticAlgorithm.rand.randint(0, num_genes - 1)
        gene = ind.genome[cut]
        ind.genome = np.delete(ind.genome, cut)
        ind.genome = np.insert(ind.genome, 0, gene)

    def __str__(self):
        return "Mutation 2 (" + f'{self.probability}' + ")"
