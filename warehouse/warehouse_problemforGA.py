from ga.problem import Problem
from warehouse.warehouse_agent_search import WarehouseAgentSearch
from warehouse.warehouse_individual import WarehouseIndividual


class WarehouseProblemGA(Problem):
    SIMPLE_FITNESS = 0
    PENALTY_FITNESS = 1

    def __init__(self, agent_search: WarehouseAgentSearch):
        super().__init__()  # Chama o método __init__ da superclasse Problem
        self.forklifts = agent_search.forklifts
        self.products = agent_search.products
        self.agent_search = agent_search

    def generate_individual(self) -> "WarehouseIndividual":
        new_individual = WarehouseIndividual(self, len(self.products) + len(self.forklifts) - 1)
        return new_individual

    def __str__(self):
        string = "# of forklifts: "
        string += f'{len(self.forklifts)}'
        string = "# of products: "
        string += f'{len(self.products)}'
        return string

    def get_pair_value(self, cell1, cell2):
        # Implemente o cálculo do valor do par de células (cell1, cell2)
        # Retorna o valor do par de células
        return self.agent_search.pairs[cell1][cell2]