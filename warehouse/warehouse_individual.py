from ga.individual_int_vector import IntVectorIndividual


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        self.products = None

        # TODO

    def compute_fitness(self) -> float:
        # TODO
        # Fitness será calculado baseado na quantidade de produtos que o agente apanhou. Quantos mais, melhor
        for i in range(self.num_genes):
            if self.genome[i]:  # == True
                self.products += self.problem.warehouse_items[i].products
        match self.problem.fitness_type:
            case self.problem.SIMPLE_FITNESS:
                self.fitness = self.products
            case self.problem.PENALTY_FITNESS:
                penalty = 0
                # TODO
                self.fitness = self.products - penalty
        return self.fitness

    def obtain_all_path(self):
        # TODO o que fazer aqui?
        pass

    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += str(self.genome) + "\n\n"
        # TODO
        return string

    def better_than(self, other: "WarehouseIndividual") -> bool:
        return True if self.fitness < other.fitness else False

    # __deepcopy__ is implemented here so that all individuals share the same problem instance
    def __deepcopy__(self, memo):
        new_instance = self.__class__(self.problem, self.num_genes)
        new_instance.genome = self.genome.copy()
        new_instance.fitness = self.fitness
        # TODO
        return new_instance
