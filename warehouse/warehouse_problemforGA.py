from ga.problem import Problem
from warehouse.warehouse_agent_search import WarehouseAgentSearch
from warehouse.warehouse_individual import WarehouseIndividual


class WarehouseProblemGA(Problem):
    SIMPLE_FITNESS = 0
    PENALTY_FITNESS = 1

    def __init__(self, agent_search: WarehouseAgentSearch):
        # TODO
        self.forklifts = agent_search.forklifts
        self.products = agent_search.products
        self.agent_search = agent_search
        # self.prob1s = prob1s -> necessita de parametro ?
        self.fitness_type = self.SIMPLE_FITNESS

    def generate_individual(self) -> "WarehouseIndividual":
        # TODO
        #                                                   VVVVVVVV
        new_individual = WarehouseIndividual(self, len(self.products))
        new_individual.initialize(self.prob1s)
        return new_individual

    def __str__(self):
        string = "# of forklifts: "
        string += f'{len(self.forklifts)}'
        string = "# of products: "
        string += f'{len(self.products)}'
        return string
