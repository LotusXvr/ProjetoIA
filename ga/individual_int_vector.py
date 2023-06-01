from abc import abstractmethod

import numpy as np

from ga.individual import Individual
from ga.problem import Problem


class IntVectorIndividual(Individual):

    def __init__(self, problem: Problem, num_genes: int):
        super().__init__(problem, num_genes)
        # TODO
        # preencher com a quantidade de produtos + agentes e shuffle
        self.genome = np.full(num_genes, False, dtype=int)
        self.genome[:num_genes] = np.arange(1, num_genes+1)
        np.random.shuffle(self.genome)
        print("Genoma -> " + str(self.genome))


    def swap_genes(self, other, index: int):
        aux = self.genome[index]
        self.genome[index] = other.genome[index]
        other.genome[index] = aux

    @abstractmethod
    def compute_fitness(self) -> float:
        pass

    @abstractmethod
    def better_than(self, other: "IntVectorIndividual") -> bool:
        pass
