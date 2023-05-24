from ga.genetic_algorithm import GeneticAlgorithm
from ga.genetic_operators.mutation import Mutation
from ga.individual_int_vector import IntVectorIndividual


class Mutation2(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        # TODO
        for gene in ind:
            if GeneticAlgorithm.rand.random() < self.probability:
                gene = 1 - gene
            ind.genome = gene

    def __str__(self):
        return "Mutation 2 (" + f'{self.probability}' + ")"
