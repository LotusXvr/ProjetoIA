from ga.genetic_algorithm import GeneticAlgorithm
from ga.genetic_operators.mutation import Mutation
from ga.individual_int_vector import IntVectorIndividual


class Mutation3(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        # TODO
        for gene in ind:
            if GeneticAlgorithm.rand.random() < self.probability:
                gene = GeneticAlgorithm.rand.randint(0, 1)  # 1 é o gene range
            ind.genome = gene

    def __str__(self):
        return "Mutation 3 (" + f'{self.probability}' + ")"
